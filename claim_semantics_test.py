import os
import tempfile

from store import EffectStore


def main():
    fd, path = tempfile.mkstemp(
        prefix="omega_claim_",
        suffix=".db",
    )
    os.close(fd)

    try:
        store = EffectStore(path)

        effect = {
            "effect_id": "E1",
            "type": "test",
            "data": "X",
        }

        # 1. 未存在
        print(
            "INITIAL:",
            store.get_status("E1"),
        )

        claimed = store.claim_execution("E1")

        print(
            "CLAIM_FROM_NONE:",
            claimed,
            store.get_status("E1"),
            store.get_effect("E1"),
        )

        # 2. PENDING
        claimed = store.claim_execution("E1")

        print(
            "CLAIM_FROM_PENDING:",
            claimed,
            store.get_status("E1"),
        )

        # 3. FAILED
        store.set_status("E1", "FAILED")

        claimed = store.claim_execution("E1")

        print(
            "CLAIM_FROM_FAILED:",
            claimed,
            store.get_status("E1"),
        )

        # 4. SUCCEEDED
        store.set_status("E1", "SUCCEEDED")

        claimed = store.claim_execution("E1")

        print(
            "CLAIM_FROM_SUCCEEDED:",
            claimed,
            store.get_status("E1"),
        )

        # 5. save_effect後のPENDING
        effect2 = {
            "effect_id": "E2",
            "type": "test",
            "data": "Y",
        }

        store.save_effect(effect2)

        claimed = store.claim_execution("E2")

        print(
            "CLAIM_AFTER_SAVE_EFFECT:",
            claimed,
            store.get_status("E2"),
            store.get_effect("E2"),
        )

        store.close()

    finally:
        if os.path.exists(path):
            os.remove(path)


if __name__ == "__main__":
    main()
