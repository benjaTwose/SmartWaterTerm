# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a db connection to sqlite db """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        prinet(e)
    finally:
        conn.close()


if __name__ == '__main__':
    create_connection("dbtest.db")
  
