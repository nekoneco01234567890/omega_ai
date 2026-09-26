import os
import tempfile

from core import OmegaCore
from recovery_capability import RecoveryCapability
from runtime import Runtime
from store import EffectStore


def run_case(name, external_status):
    fd, path = tempfile.mkstemp(
        prefix="omega_cap_runtime_",
        suffix=".db",
    )
    os.close(fd)

    try:
        core = OmegaCore(goal="capability_runtime")

        _, effects = core.step(name)
        effect = effects[0]

        capability = RecoveryCapability(
            external_status=external_status,
        )

        store = EffectStore(path)
        runtime = Runtime(
            store,
            capability=capability,
        )

        result = runtime.execute_effect(effect)

        print(
            name,
            {
                "result": result,
                "execute_count": capability.execute_count,
                "status": store.get_status(
                    effect["effect_id"]
                ),
                "effect_restored":
                    store.get_effect(
                        effect["effect_id"]
                    ) == effect,
            },
        )

        store.close()

    finally:
        if os.path.exists(path):
            os.remove(path)


def main():
    print("=== CAPABILITY RUNTIME INTEGRATION ===")

    run_case(
        "NOT_EXECUTED",
        "NOT_EXECUTED",
    )

    run_case(
        "EXECUTED",
        "EXECUTED",
    )

    run_case(
        "UNKNOWN",
        "UNKNOWN",
    )


if __name__ == "__main__":
    main()
