import json
import os
import tempfile

from core import OmegaCore
from state_store import StateStore
from store import EffectStore


def fresh_paths():
    state_fd, state_path = tempfile.mkstemp(
        prefix="omega_matrix_state_",
        suffix=".json",
    )
    os.close(state_fd)

    db_fd, db_path = tempfile.mkstemp(
        prefix="omega_matrix_db_",
        suffix=".db",
    )
    os.close(db_fd)

    return state_path, db_path


def scenario(name, save_effect, save_state):
    state_path, db_path = fresh_paths()

    try:
        core = OmegaCore(goal="crash_matrix")
        core.step("OBSERVATION")

        effect = core.step("NEXT")[1][0]

        state_store = StateStore(state_path)
        effect_store = EffectStore(db_path)

        # --------------------------------------------------
        # 模擬クラッシュ前の永続化順序
        # --------------------------------------------------
        if save_effect:
            effect_store.save_effect(effect)

        if save_state:
            state_store.save(core.get_state())

        # プロセス完全終了を模擬
        effect_store.close()

        # --------------------------------------------------
        # 再起動
        # --------------------------------------------------
        restarted_state_store = StateStore(state_path)
        restarted_effect_store = EffectStore(db_path)

        try:
            restored_state = restarted_state_store.load()
            state_restored = True
        except Exception:
            restored_state = None
            state_restored = False

        restored_effect = restarted_effect_store.get_effect(
            effect["effect_id"]
        )

        effect_restored = (
            restored_effect == effect
        )

        print(
            name,
            {
                "state_restored": state_restored,
                "effect_restored": effect_restored,
                "effect_status": restarted_effect_store.get_status(
                    effect["effect_id"]
                ),
            },
        )

        restarted_state_store  # 意図的に保持
        restarted_effect_store.close()

    finally:
        if os.path.exists(state_path):
            os.remove(state_path)

        if os.path.exists(db_path):
            os.remove(db_path)


def main():
    print("=== CRASH BOUNDARY MATRIX ===")

    scenario(
        "CRASH_BEFORE_EFFECT_SAVE",
        save_effect=False,
        save_state=False,
    )

    scenario(
        "EFFECT_SAVED_STATE_NOT_SAVED",
        save_effect=True,
        save_state=False,
    )

    scenario(
        "STATE_SAVED_EFFECT_NOT_SAVED",
        save_effect=False,
        save_state=True,
    )

    scenario(
        "BOTH_SAVED",
        save_effect=True,
        save_state=True,
    )


if __name__ == "__main__":
    main()
