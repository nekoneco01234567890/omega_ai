import hashlib
import json
from typing import Any


def canonical_hash(data: Any) -> str:
    raw = json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(raw.encode()).hexdigest()


def payload_hash(record: dict[str, Any]) -> str:
    payload = {
        "event_id": record["event_id"],
        "type": record["type"],
        "data": record["data"],
        "seq": record["seq"],
    }

    return canonical_hash(payload)


def chain_hash(
    previous_hash: str,
    record: dict[str, Any],
) -> str:
    raw = (
        previous_hash
        + str(record["seq"])
        + record["payload_hash"]
    )

    return hashlib.sha256(raw.encode()).hexdigest()


def semantic_state_payload(data: dict[str, Any]) -> dict[str, Any]:
    return {
        "goal": data["goal"],
        "world_state": data["world_state"],
        "facts": data["facts"],
        "hypotheses": data["hypotheses"],
        "results": data["results"],
        "unknowns": data["unknowns"],
    }


def state_hash(data: dict[str, Any]) -> str:
    return canonical_hash(
        semantic_state_payload(data)
    )


def build_audit(
    history: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:

    audited = []
    previous_hash = ""

    for seq, event in enumerate(history):
        record = {
            "seq": seq,
            "event_id": event["event_id"],
            "type": event["type"],
            "data": event["data"],
        }

        record["payload_hash"] = payload_hash(record)

        record["chain_hash"] = chain_hash(
            previous_hash,
            record,
        )

        previous_hash = record["chain_hash"]
        audited.append(record)

    terminal = {
        "completed": True,
        "last_seq": len(audited) - 1,
        "final_chain_hash": (
            audited[-1]["chain_hash"]
            if audited
            else ""
        ),
    }

    return audited, terminal


def verify(
    history: list[dict[str, Any]],
    terminal: dict[str, Any],
) -> bool:

    if not terminal.get("completed"):
        return False

    if terminal.get("last_seq") != len(history) - 1:
        return False

    previous_hash = ""

    for expected_seq, record in enumerate(history):
        if record.get("seq") != expected_seq:
            return False

        if record.get("payload_hash") != payload_hash(record):
            return False

        expected_chain = chain_hash(
            previous_hash,
            record,
        )

        if record.get("chain_hash") != expected_chain:
            return False

        previous_hash = expected_chain

    if terminal.get("final_chain_hash") != previous_hash:
        return False

    return True
