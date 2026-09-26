import os
import tempfile

from recovery_capability import RecoveryCapability
from store import EffectStore


def run_case(name, external_status, execute_success=True):
    fd, path = tempfile.mkstemp(
        prefix="omega_pending_resolution_",
        suffix=".db",
    )
    os.close(fd)

    try:
        store = EffectStore(path)

        effect = {
            "effect_id": name,
            "type": "test",
            "data": "X",
        }

        store.save_effect(effect)

        capability = RecoveryCapability(
            external_status=external_status,
            execute_success=execute_success,
        )

        before = store.get_status(effect["effect_id"])

        # 現在のRecovery経路を直接実行
        result = None

        status = store.get_status(effect["effect_id"])

        if status == "PENDING":
            external = capability.query(effect)

            if external == "EXECUTED":
                store.set_status(
                    effect["effect_id"],
                    "SUCCEEDED",
                )
                result = "confirmed_executed"

            elif external == "NOT_EXECUTED":
                executed = capability.execute(effect)

                if executed:
                    store.set_status(
                        effect["effect_id"],
                        "SUCCEEDED",
                    )
                    result = "executed"

                else:
                    result = "execution_failed"

            elif external == "UNKNOWN":
                result = "remain_pending"

            else:
                result = "invalid_external_status"

        print(
            name,
            {
                "before": before,
                "query": external_status,
                "result": result,
                "execute_count": capability.execute_count,
                "final": store.get_status(
                    effect["effect_id"]
                ),
            },
        )

        store.close()

    finally:
        if os.path.exists(path):
            os.remove(path)


def main():
    print("=== PENDING RESOLUTION ===")

    run_case(
        "NEW_EXTERNAL_UNKNOWN",
        "UNKNOWN",
    )

    run_case(
        "NEW_EXTERNAL_NOT_EXECUTED",
        "NOT_EXECUTED",
    )

    run_case(
        "NEW_EXTERNAL_EXECUTED",
        "EXECUTED",
    )

    run_case(
        "CRASH_EXTERNAL_EXECUTED",
        "EXECUTED",
    )

    run_case(
        "CRASH_EXTERNAL_NOT_EXECUTED",
        "NOT_EXECUTED",
    )

    run_case(
        "CRASH_EXTERNAL_UNKNOWN",
        "UNKNOWN",
    )

    run_case(
        "NOT_EXECUTED_BUT_REEXECUTION_FAILS",
        "NOT_EXECUTED",
        execute_success=False,
    )


if __name__ == "__main__":
    main()
