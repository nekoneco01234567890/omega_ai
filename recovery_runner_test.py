import os
import tempfile

from recovery_runner import RecoveryRunner
from recovery_capability import RecoveryCapability
from store import EffectStore


def prepare_store(path):
    store = EffectStore(path)

    store.save_effect({"effect_id": "E1", "type": "test", "data": "A"})
    store.save_effect({"effect_id": "E2", "type": "test", "data": "B"})

    store.claim_execution("E1")
    store.claim_execution("E2")

    store.close()


def run_case(name, external_status):
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)

    try:
        prepare_store(path)

        store = EffectStore(path)
        capability = RecoveryCapability(external_status=external_status)

        runner = RecoveryRunner(store, capability)
        results = runner.recover_all()

        statuses = {
            "E1": store.get_status("E1"),
            "E2": store.get_status("E2"),
        }

        print(name)
        print("RESULTS:", results)
        print("STATUSES:", statuses)

        store.close()

    finally:
        if os.path.exists(path):
            os.remove(path)


def main():
    print("=== RECOVERY RUNNER TEST ===")

    run_case("EXECUTED", "EXECUTED")
    run_case("NOT_EXECUTED", "NOT_EXECUTED")
    run_case("UNKNOWN", "UNKNOWN")


if __name__ == "__main__":
    main()
