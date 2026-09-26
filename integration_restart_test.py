import os
import tempfile
from copy import deepcopy

from core import OmegaCore
from recovery_capability import RecoveryCapability
from runtime import Runtime
from state_store import StateStore
from store import EffectStore


def main():
    state_fd, state_path = tempfile.mkstemp(
        prefix="omega_state_",
        suffix=".json",
    )
    os.close(state_fd)

    db_fd, db_path = tempfile.mkstemp(
        prefix="omega_runtime_",
        suffix=".db",
    )
    os.close(db_fd)

    try:
        # ==================================================
        # Phase 1: Core -> State persistence
        # ==================================================
        core = OmegaCore(goal="restart_integration")

        core.step("A")

        state_store = StateStore(state_path)
        state_store.save(core.get_state())

        original_state = deepcopy(
            core.get_state()
        )

        effect = core.step("B")[1][0]

        # B反映後のStateも保存
        state_store.save(core.get_state())

        print(
            "PHASE1_STATE_SAVE:",
            True,
        )

        # ==================================================
        # Phase 2: Runtime executes effect,
        # then crashes after external execution
        # ==================================================
        store1 = EffectStore(db_path)
        runtime1 = Runtime(store1)

        try:
            runtime1.execute_effect(
                effect,
                crash_after_external=True,
            )
        except RuntimeError as e:
            print(
                "EXPECTED_CRASH:",
                str(e),
            )

        pending_status = store1.get_status(
            effect["effect_id"]
        )

        print(
            "PENDING_PERSISTED:",
            pending_status == "PENDING",
        )

        store1.close()

        # ==================================================
        # Phase 3: Process restart
        # ==================================================
        restored_state = state_store.load()

        print(
            "STATE_RESTORED_AFTER_RESTART:",
            restored_state == core.get_state(),
        )

        # Runtimeも再生成
        store2 = EffectStore(db_path)
        runtime2 = Runtime(store2)

        # 外部世界を照会した結果、
        # crash前に実行済みだったことが判明
        capability = RecoveryCapability(
            external_status="EXECUTED"
        )

        recovery = runtime2.recover_effect(
            effect,
            capability,
        )

        print(
            "RECOVERY_STATUS:",
            recovery["status"],
        )

        print(
            "RECOVERY_ACTION:",
            recovery["action"],
        )

        print(
            "FINAL_EFFECT_STATUS:",
            store2.get_status(
                effect["effect_id"]
            ),
        )

        # ==================================================
        # Phase 4: State Integrity tamper rejection
        # ==================================================
        import json

        with open(
            state_path,
            "r",
            encoding="utf-8",
        ) as f:
            data = json.load(f)

        data["facts"].append("TAMPERED")

        with open(
            state_path,
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                sort_keys=True,
            )

        try:
            state_store.load()
            print(
                "TAMPERED_STATE_ACCEPTED: True"
            )
        except ValueError as e:
            print(
                "TAMPERED_STATE_REJECTED:",
                str(e),
            )

        store2.close()

    finally:
        if os.path.exists(state_path):
            os.remove(state_path)

        if os.path.exists(db_path):
            os.remove(db_path)


if __name__ == "__main__":
    main()
