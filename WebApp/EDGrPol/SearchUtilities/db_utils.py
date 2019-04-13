import os
from django.db import connection

NAME = 'GrPolDict.db'


class Database:
    def __init__(self):
        self.cur = connection.cursor()

    def commit(self):
        self.cur.commit()

    def execute(self, q, arg):
        if arg != 0:
            self.cur.execute(q, arg)
        else:
            self.cur.execute(q)
        res = self.cur.fetchall()
        self.cur.close()
        return res
