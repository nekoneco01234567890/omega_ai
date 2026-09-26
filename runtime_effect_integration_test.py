import os
import tempfile

from core import OmegaCore
from runtime import Runtime
from store import EffectStore


def main():
    fd, path = tempfile.mkstemp(
        prefix="omega_runtime_effect_",
        suffix=".db",
    )
    os.close(fd)

    try:
        core = OmegaCore(goal="runtime_effect_integration")

        _, effects = core.step("OBSERVATION")
        effect = effects[0]

        store = EffectStore(path)
        runtime = Runtime(store)

        # Effectを永続化
        store.save_effect(effect)

        print(
            "AFTER_SAVE:",
            store.get_status(effect["effect_id"]),
            store.get_effect(effect["effect_id"]) == effect,
        )

        # Runtimeから実行
        result = runtime.execute_effect(effect)

        print(
            "EXECUTE_RESULT:",
            result,
        )

        print(
            "FINAL_STATUS:",
            store.get_status(effect["effect_id"]),
        )

        # 同じEffectをもう一度
        second = runtime.execute_effect(effect)

        print(
            "SECOND_EXECUTE:",
            second,
        )

        print(
            "FINAL_STATUS_AFTER_SECOND:",
            store.get_status(effect["effect_id"]),
        )

        store.close()

    finally:
        if os.path.exists(path):
            os.remove(path)


if __name__ == "__main__":
    main()
