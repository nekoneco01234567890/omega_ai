import os
import tempfile
import json

from store import EffectStore


def snapshot(store, effect_id):
    return {
        "effect": store.get_effect(effect_id),
        "status": store.get_status(effect_id),
    }


def main():
    fd, path = tempfile.mkstemp(
        prefix="omega_pending_ambiguity_",
        suffix=".db",
    )
    os.close(fd)

    try:
        effect = {
            "effect_id": "E1",
            "type": "test",
            "data": "X",
        }

        # --------------------------------------------------
        # CASE A
        # 新規Effectを保存しただけ
        # --------------------------------------------------
        store = EffectStore(path)
        store.save_effect(effect)

        case_a = snapshot(store, "E1")

        print("CASE_A_NEW_PENDING:")
        print(json.dumps(case_a, ensure_ascii=False, sort_keys=True))

        store.close()

        # --------------------------------------------------
        # CASE B
        # PENDINGから外部作用が発生したが、
        # SUCCEEDED保存前にCrashした状態
        # --------------------------------------------------
        store = EffectStore(path)

        # DBを一旦作り直すため別Effect ID
        effect_b = {
            "effect_id": "E2",
            "type": "test",
            "data": "X",
        }

        store.save_effect(effect_b)

        # 現在のclaimはPENDINGから拒否されるため、
        # 「外部作用後Crash」を現在のDB表現として作るには
        # PENDINGのままにするしかない。
        #
        # つまり、ここでDB上の情報は
        # Case Aと同じ構造になる。

        case_b = snapshot(store, "E2")

        print("CASE_B_EXTERNAL_EXECUTED_PENDING:")
        print(json.dumps(case_b, ensure_ascii=False, sort_keys=True))

        store.close()

        # --------------------------------------------------
        # DB上で区別可能な情報があるか確認
        # --------------------------------------------------
        comparable_a = {
            "status": case_a["status"],
            "effect": case_a["effect"],
        }

        comparable_b = {
            "status": case_b["status"],
            "effect": case_b["effect"],
        }

        # IDだけ違うので正規化
        comparable_a["effect"]["effect_id"] = "NORMALIZED"
        comparable_b["effect"]["effect_id"] = "NORMALIZED"

        print(
            "PERSISTED_REPRESENTATION_IDENTICAL:",
            comparable_a == comparable_b,
        )

    finally:
        if os.path.exists(path):
            os.remove(path)


if __name__ == "__main__":
    main()
