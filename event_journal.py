import hashlib
import json
import sqlite3


class EventJournal:
    def __init__(self, path="event_journal.db"):
        self.conn = sqlite3.connect(path)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS journal(
                seq INTEGER PRIMARY KEY,
                event_json TEXT NOT NULL,
                chain_hash TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def append(self, event: dict):
        last = self.conn.execute(
            "SELECT seq, chain_hash FROM journal ORDER BY seq DESC LIMIT 1"
        ).fetchone()

        seq = 0 if last is None else last[0] + 1
        previous = "" if last is None else last[1]

        event_json = json.dumps(
            event,
            sort_keys=True,
            ensure_ascii=False,
        )

        chain_hash = hashlib.sha256(
            (previous + str(seq) + event_json).encode()
        ).hexdigest()

        self.conn.execute(
            "INSERT INTO journal(seq,event_json,chain_hash) VALUES(?,?,?)",
            (seq, event_json, chain_hash),
        )
        self.conn.commit()

    def verify(self):
        rows = self.conn.execute(
            """
            SELECT seq, event_json, chain_hash
            FROM journal
            ORDER BY seq
            """
        ).fetchall()

        previous_hash = ""

        for expected_seq, (seq, event_json, chain_hash) in enumerate(rows):
            if seq != expected_seq:
                return False

            expected_chain = hashlib.sha256(
                (previous_hash + str(seq) + event_json).encode()
            ).hexdigest()

            if chain_hash != expected_chain:
                return False

            previous_hash = chain_hash

        return True

    def close(self):
        self.conn.close()
