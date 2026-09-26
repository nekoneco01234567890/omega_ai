import os
import tempfile

from core import OmegaCore
from store import EffectStore


def main():
    fd, path = tempfile.mkstemp(
        prefix="omega_effect_",
        suffix=".db",
    )
    os.close(fd)

    try:
        # ==============================================
        # Process 1
        # ==============================================
        core = OmegaCore(goal="effect_persistence")

        _, effects = core.step("OBSERVATION")

        effect = effects[0]
        effect_id = effect["effect_id"]

        store1 = EffectStore(path)

        store1.save_effect(effect)

        print(
            "EFFECT_SAVED:",
            True,
        )

        print(
            "ORIGINAL_EFFECT:",
            effect,
        )

        store1.close()

        # ==============================================
        # Process 2
        # 完全に再生成
        # ==============================================
        store2 = EffectStore(path)

        restored_effect = store2.get_effect(
            effect_id
        )

        print(
            "EFFECT_RESTORED:",
            restored_effect == effect,
        )

        print(
            "STATUS_RESTORED:",
            store2.get_status(effect_id),
        )

        # メモリ上の元Effectを捨てた状態でも
        # DBから復元できることを確認
        del effect
        del effects
        del core

        restored_again = store2.get_effect(
            effect_id
        )

        print(
            "MEMORY_INDEPENDENT_RESTORE:",
            restored_again == restored_effect,
        )

        store2.close()

    finally:
        if os.path.exists(path):
            os.remove(path)


if __name__ == "__main__":
    main()
