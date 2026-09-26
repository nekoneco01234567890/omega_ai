import json
import os
import tempfile
from copy import deepcopy

from core import OmegaCore
from state_store import StateStore


FIELDS = [
    "goal",
    "world_state",
    "facts",
    "hypotheses",
    "results",
    "unknowns",
]


def make_core():
    core = OmegaCore(goal="integration_test")

    core.state.world_state["market"] = "open"
    core.state.facts.append("FACT_A")
    core.state.hypotheses.append("HYPOTHESIS_A")
    core.state.results.append("RESULT_A")
    core.state.unknowns.append("UNKNOWN_A")

    core.step("A")
    core.step("B")
    core.step("C")

    return core


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            sort_keys=True,
        )


def main():
    fd, path = tempfile.mkstemp(
        prefix="omega_state_",
        suffix=".json",
    )
    os.close(fd)

    try:
        core = make_core()
        original_state = deepcopy(core.get_state())

        store = StateStore(path)
        store.save(core.get_state())

        restored = store.load()

        print(
            "NORMAL_RESTORE:",
            restored == original_state,
        )

        # 各Stateフィールドを個別改ざん
        for field in FIELDS:
            data = load_json(path)

            if field == "goal":
                data[field] = "TAMPERED"

            elif field == "world_state":
                data[field]["market"] = "TAMPERED"

            else:
                data[field].append("TAMPERED")

            save_json(path, data)

            try:
                store.load()
                print(
                    f"{field.upper()}_TAMPER_ACCEPTED: True"
                )
            except ValueError as e:
                print(
                    f"{field.upper()}_TAMPER_REJECTED:",
                    str(e),
                )

        # history改ざん
        store.save(core.get_state())
        data = load_json(path)

        data["history"][1]["data"] = "TAMPERED"
        save_json(path, data)

        try:
            store.load()
            print("HISTORY_TAMPER_ACCEPTED: True")
        except ValueError as e:
            print(
                "HISTORY_TAMPER_REJECTED:",
                str(e),
            )

        # 正常状態へ戻して最終確認
        store.save(core.get_state())
        final_state = store.load()

        print(
            "FINAL_VALID_RESTORE:",
            final_state == original_state,
        )

    finally:
        if os.path.exists(path):
            os.remove(path)


if __name__ == "__main__":
    main()
