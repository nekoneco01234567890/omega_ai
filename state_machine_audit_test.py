import os
import tempfile

from store import EffectStore


def main():
    fd, path = tempfile.mkstemp(
        prefix="omega_state_machine_",
        suffix=".db",
    )
    os.close(fd)

    try:
        store = EffectStore(path)

        effect = {
            "effect_id": "AUDIT-1",
            "type": "test",
            "data": "X",
        }

        print("INITIAL:", store.get_status("AUDIT-1"))

        store.save_effect(effect)

        print(
            "AFTER_SAVE:",
            store.get_status("AUDIT-1"),
            store.get_effect("AUDIT-1") == effect,
        )

        print(
            "CLAIM_AFTER_SAVE:",
            store.claim_execution("AUDIT-1"),
            store.get_status("AUDIT-1"),
        )

        store.set_status("AUDIT-1", "FAILED")

        print(
            "AFTER_FAILED:",
            store.get_status("AUDIT-1"),
        )

        print(
            "CLAIM_AFTER_FAILED:",
            store.claim_execution("AUDIT-1"),
            store.get_status("AUDIT-1"),
        )

        store.set_status("AUDIT-1", "SUCCEEDED")

        print(
            "AFTER_SUCCEEDED:",
            store.get_status("AUDIT-1"),
        )

        print(
            "CLAIM_AFTER_SUCCEEDED:",
            store.claim_execution("AUDIT-1"),
            store.get_status("AUDIT-1"),
        )

        store.close()

    finally:
        if os.path.exists(path):
            os.remove(path)


if __name__ == "__main__":
    main()
