from runtime import Runtime
from store import EffectStore


class RecoveryRunner:
    def __init__(self, store: EffectStore, capability):
        self.store = store
        self.runtime = Runtime(store)
        self.capability = capability

    def recover_all(self):
        results = []

        for effect in self.store.list_pending_effects():
            result = self.runtime.recover_effect(
                effect,
                self.capability,
            )

            results.append({
                "effect_id": effect["effect_id"],
                **result,
            })

        return results
