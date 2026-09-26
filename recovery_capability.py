from typing import Any


class RecoveryCapability:
    def __init__(
        self,
        external_status: str,
        execute_success: bool = True,
        crash_after_execute: bool = False,
    ):
        self.external_status = external_status
        self.execute_success = execute_success
        self.crash_after_execute = crash_after_execute
        self.execute_count = 0

    def query(self, effect: dict[str, Any]) -> str:
        return self.external_status

    def execute(self, effect: dict[str, Any]) -> bool:
        self.execute_count += 1

        if not self.execute_success:
            return False

        if self.crash_after_execute:
            raise RuntimeError(
                "SIMULATED_RECOVERY_CRASH_AFTER_EXTERNAL"
            )

        return True
