import json
import os
import tempfile

from integrity import (
    build_audit,
    state_hash,
    verify,
)
from state import AIState


class StateStore:
    def __init__(self, path: str):
        self.path = path

    def save(self, state: AIState) -> None:
        data = {
            "goal": state.goal,
            "world_state": state.world_state,
            "facts": state.facts,
            "hypotheses": state.hypotheses,
            "results": state.results,
            "unknowns": state.unknowns,
        }

        audited_history, terminal = build_audit(
            state.history
        )

        data["history"] = audited_history
        data["terminal"] = terminal
        data["state_hash"] = state_hash(data)

        directory = os.path.dirname(self.path) or "."

        fd, temp_path = tempfile.mkstemp(
            prefix=".omega_state_",
            dir=directory,
            suffix=".json",
        )

        try:
            with os.fdopen(
                fd,
                "w",
                encoding="utf-8",
            ) as f:
                json.dump(
                    data,
                    f,
                    ensure_ascii=False,
                    sort_keys=True,
                )
                f.flush()
                os.fsync(f.fileno())

            os.replace(temp_path, self.path)
            temp_path = None

        finally:
            if (
                temp_path is not None
                and os.path.exists(temp_path)
            ):
                os.remove(temp_path)

    def load(self) -> AIState:
        with open(
            self.path,
            "r",
            encoding="utf-8",
        ) as f:
            data = json.load(f)

        if not verify(
            data["history"],
            data["terminal"],
        ):
            raise ValueError(
                "INTEGRITY_VERIFICATION_FAILED"
            )

        if data.get("state_hash") != state_hash(data):
            raise ValueError(
                "STATE_INTEGRITY_VERIFICATION_FAILED"
            )

        semantic_history = [
            {
                "event_id": record["event_id"],
                "type": record["type"],
                "data": record["data"],
            }
            for record in data["history"]
        ]

        return AIState(
            goal=data["goal"],
            world_state=data["world_state"],
            facts=data["facts"],
            hypotheses=data["hypotheses"],
            results=data["results"],
            unknowns=data["unknowns"],
            history=semantic_history,
        )
