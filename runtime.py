from typing import Any

from store import EffectStore


class Runtime:
    def __init__(
        self,
        store: EffectStore,
        capability: Any = None,
    ):
        self.store = store
        self.capability = capability

    def execute_effect(
        self,
        effect: dict[str, Any],
        fail: bool = False,
        crash_after_external: bool = False,
    ) -> dict[str, Any]:

        effect_id = effect["effect_id"]

        # Effect本体を永続化（新規なら READY、既存なら保持）
        self.store.save_effect(effect)

        status = self.store.get_status(effect_id)

        if status == "SUCCEEDED":
            return {
                "executed": False,
                "status": "already_processed",
            }

        # READY -> PENDING
        claimed = self.store.claim_execution(effect_id)

        if not claimed:
            status = self.store.get_status(effect_id)

            if status == "SUCCEEDED":
                return {
                    "executed": False,
                    "status": "already_processed",
                }

            return {
                "executed": False,
                "status": "recovery_required",
            }

        # Capability付き通常実行
        if self.capability is not None:
            external_status = self.capability.query(effect)

            if external_status == "EXECUTED":
                self.store.set_status(effect_id, "SUCCEEDED")
                return {
                    "executed": False,
                    "status": "already_executed",
                }

            if external_status == "UNKNOWN":
                return {
                    "executed": False,
                    "status": "recovery_required",
                }

            if external_status != "NOT_EXECUTED":
                return {
                    "executed": False,
                    "status": "invalid_external_status",
                }

            executed = self.capability.execute(effect)

            if executed is not True:
                return {
                    "executed": False,
                    "status": "execution_failed",
                }

            self.store.set_status(effect_id, "SUCCEEDED")

            return {
                "executed": True,
                "status": "executed",
            }

        # Capabilityなし通常実行
        if fail:
            self.store.set_status(effect_id, "FAILED")
            return {
                "executed": False,
                "status": "execution_failed",
            }

        if crash_after_external:
            raise RuntimeError(
                "SIMULATED_CRASH_AFTER_EXTERNAL"
            )

        self.store.set_status(effect_id, "SUCCEEDED")

        return {
            "executed": True,
            "status": "executed",
        }

    def recover_effect(
        self,
        effect: dict[str, Any],
        capability: Any,
    ) -> dict[str, Any]:

        effect_id = effect["effect_id"]
        status = self.store.get_status(effect_id)

        if status != "PENDING":
            return {
                "recovered": False,
                "status": "not_recoverable",
                "current_status": status,
            }

        external_status = capability.query(effect)

        if external_status == "EXECUTED":
            self.store.set_status(effect_id, "SUCCEEDED")
            return {
                "recovered": True,
                "status": "succeeded",
                "action": "confirmed_executed",
            }

        if external_status == "NOT_EXECUTED":
            executed = capability.execute(effect)

            if executed is True:
                self.store.set_status(effect_id, "SUCCEEDED")
                return {
                    "recovered": True,
                    "status": "succeeded",
                    "action": "reexecuted",
                }

            return {
                "recovered": False,
                "status": "execution_failed",
                "action": "reexecution_failed",
            }

        if external_status == "UNKNOWN":
            return {
                "recovered": False,
                "status": "recovery_required",
                "action": "remain_pending",
            }

        return {
            "recovered": False,
            "status": "invalid_external_status",
            "action": "remain_pending",
        }

