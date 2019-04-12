import sqlite3
import os

NAME = 'GrPolDict.db'


class Database:
    def __init__(self):
        self._connection = sqlite3.connect(os.path.join("..", "..", NAME))

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
