import os
import sqlite3
import tempfile

from event_journal import EventJournal


def read_rows(path):
    conn = sqlite3.connect(path)
    rows = conn.execute(
        "SELECT seq, event_json, chain_hash FROM journal ORDER BY seq"
    ).fetchall()
    conn.close()
    return rows


def main():
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)

    try:
        journal = EventJournal(path)

        journal.append({"event_id": "E1", "type": "obs", "data": "A"})
        journal.append({"event_id": "E2", "type": "obs", "data": "B"})
        journal.append({"event_id": "E3", "type": "obs", "data": "C"})

        rows = read_rows(path)

        print("ROW_COUNT:", len(rows))
        print("SEQUENCE:", [r[0] for r in rows])

        print("FIRST_HASH_EXISTS:", rows[0][2] != "")
        print("LAST_HASH_EXISTS:", rows[-1][2] != "")

    finally:
        if os.path.exists(path):
            os.remove(path)


if __name__ == "__main__":
    main()
