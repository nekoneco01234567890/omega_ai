import os
import tempfile

from core import OmegaCore
from event_journal import EventJournal
from recovery_runner import RecoveryRunner
from recovery_capability import RecoveryCapability
from runtime import Runtime
from state_store import StateStore
from store import EffectStore


def main():
    state_fd, state_path = tempfile.mkstemp(suffix=".json")
    os.close(state_fd)

    effect_fd, effect_path = tempfile.mkstemp(suffix=".db")
    os.close(effect_fd)

    journal_fd, journal_path = tempfile.mkstemp(suffix=".db")
    os.close(journal_fd)

    try:
        core = OmegaCore(goal="e2e_audit")

        state_store = StateStore(state_path)
        effect_store = EffectStore(effect_path)
        journal = EventJournal(journal_path)

        # 3イベント生成
        for value in ["A", "B", "C"]:
            state, effects = core.step(value)
            journal.append(state.history[-1])

        effect = effects[0]

        # State / Effect 保存
        state_store.save(core.get_state())
        effect_store.save_effect(effect)

        # クラッシュ前 (READY→PENDING)
        runtime = Runtime(effect_store)
        effect_store.claim_execution(effect["effect_id"])

        # 再起動を模擬
        effect_store.close()

        restored_state = state_store.load()

        restarted_store = EffectStore(effect_path)
        runner = RecoveryRunner(
            restarted_store,
            RecoveryCapability(external_status="EXECUTED"),
        )

        recovery = runner.recover_all()

        print("STATE_RESTORED:", restored_state == core.get_state())
        print("JOURNAL_VALID:", EventJournal(journal_path).verify())
        print("RECOVERY_COUNT:", len(recovery))
        print("FINAL_STATUS:", restarted_store.get_status(effect["effect_id"]))

        restarted_store.close()

    finally:
        for path in (state_path, effect_path, journal_path):
            if os.path.exists(path):
                os.remove(path)


if __name__ == "__main__":
    main()
