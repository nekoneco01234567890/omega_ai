import os
import sqlite3
import tempfile

from event_journal import EventJournal


def main():
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)

    try:
        journal = EventJournal(path)

        journal.append({"event_id": "E1", "type": "obs", "data": "A"})
        journal.append({"event_id": "E2", "type": "obs", "data": "B"})
        journal.append({"event_id": "E3", "type": "obs", "data": "C"})

        print("VALID:", journal.verify())

        journal.close()

        # event_json 改ざん
        conn = sqlite3.connect(path)
        conn.execute(
            "UPDATE journal SET event_json=? WHERE seq=1",
            ('{"event_id":"E2","type":"obs","data":"TAMPERED"}',),
        )
        conn.commit()
        conn.close()

        print("EVENT_TAMPER:", EventJournal(path).verify())

        # 正常データを作り直し
        os.remove(path)
        journal = EventJournal(path)
        journal.append({"event_id": "E1", "type": "obs", "data": "A"})
        journal.append({"event_id": "E2", "type": "obs", "data": "B"})
        journal.append({"event_id": "E3", "type": "obs", "data": "C"})
        journal.close()

        # chain_hash 改ざん
        conn = sqlite3.connect(path)
        conn.execute(
            "UPDATE journal SET chain_hash='BADHASH' WHERE seq=2"
        )
        conn.commit()
        conn.close()

        print("CHAIN_TAMPER:", EventJournal(path).verify())

    finally:
        if os.path.exists(path):
            os.remove(path)


if __name__ == "__main__":
    main()
