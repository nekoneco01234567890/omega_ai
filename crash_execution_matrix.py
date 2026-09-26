import os
import tempfile

from core import OmegaCore
from recovery_capability import RecoveryCapability
from state_store import StateStore
from store import EffectStore


def fresh_paths():
    state_fd, state_path = tempfile.mkstemp(
        prefix="omega_exec_state_",
        suffix=".json",
    )
    os.close(state_fd)

    db_fd, db_path = tempfile.mkstemp(
        prefix="omega_exec_db_",
        suffix=".db",
    )
    os.close(db_fd)

    return state_path, db_path


def inspect_after_restart(
    state_path,
    db_path,
    effect_id,
):
    state_store = StateStore(state_path)
    effect_store = EffectStore(db_path)

    try:
        try:
            state_store.load()
            state_ok = True
        except Exception:
            state_ok = False

        effect = effect_store.get_effect(effect_id)
        status = effect_store.get_status(effect_id)

        return {
            "state": state_ok,
            "effect": effect is not None,
            "status": status,
        }

    finally:
        effect_store.close()


def scenario(name, crash_point):
    state_path, db_path = fresh_paths()

    try:
        core = OmegaCore(goal="execution_matrix")
        core.step("OBSERVATION")
        state, effects = core.step("NEXT")
        effect = effects[0]

        state_store = StateStore(state_path)
        effect_store = EffectStore(db_path)

        # A: Effect生成済み
        if crash_point == "AFTER_GENERATION":
            effect_store.close()
            print(name, inspect_after_restart(
                state_path,
                db_path,
                effect["effect_id"],
            ))
            return

        # B: Effect保存
        effect_store.save_effect(effect)

        if crash_point == "AFTER_EFFECT_SAVE":
            effect_store.close()
            print(name, inspect_after_restart(
                state_path,
                db_path,
                effect["effect_id"],
            ))
            return

        # C: State保存
        state_store.save(state)

        if crash_point == "AFTER_STATE_SAVE":
            effect_store.close()
            print(name, inspect_after_restart(
                state_path,
                db_path,
                effect["effect_id"],
            ))
            return

        # D: 実行claim = PENDING
        claimed = effect_store.claim_execution(
            effect["effect_id"]
        )

        print(
            name,
            "CLAIMED:",
            claimed,
        )

        if crash_point == "AFTER_CLAIM":
            effect_store.close()
            print(name, inspect_after_restart(
                state_path,
                db_path,
                effect["effect_id"],
            ))
            return

        # E: 外部作用
        capability = RecoveryCapability(
            external_status="UNKNOWN"
        )

        executed = capability.execute(effect)

        print(
            name,
            "EXTERNAL_EXECUTED:",
            executed,
        )

        if crash_point == "AFTER_EXTERNAL":
            effect_store.close()
            print(name, inspect_after_restart(
                state_path,
                db_path,
                effect["effect_id"],
            ))
            return

        # F: 成功確定
        effect_store.set_status(
            effect["effect_id"],
            "SUCCEEDED",
        )

        if crash_point == "AFTER_SUCCESS":
            effect_store.close()
            print(name, inspect_after_restart(
                state_path,
                db_path,
                effect["effect_id"],
            ))
            return

        effect_store.close()

    finally:
        if os.path.exists(state_path):
            os.remove(state_path)

        if os.path.exists(db_path):
            os.remove(db_path)


def main():
    print("=== EXECUTION CRASH MATRIX ===")

    for point in [
        "AFTER_GENERATION",
        "AFTER_EFFECT_SAVE",
        "AFTER_STATE_SAVE",
        "AFTER_CLAIM",
        "AFTER_EXTERNAL",
        "AFTER_SUCCESS",
    ]:
        scenario(
            point,
            point,
        )


if __name__ == "__main__":
    main()
