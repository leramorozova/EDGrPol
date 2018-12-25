import sqlite3 as sql


class Database:
    def __init__(self, greek_or_pol):
        self._connection = sql.connect(greek_or_pol + "_dict.db")

    def commit(self):
        self._connection.commit()

    def execute(self, q, arg):
        cur = self._connection.cursor()
        if arg != 0:
            cur.execute(q, arg)
        else:
            cur.execute(q)
        res = cur.fetchall()
        cur.close()
        return res
