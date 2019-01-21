# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a db connection to sqlite db """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
	except Error as e:
        prinet(e)
		return None

		
def select_all_data(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM reg_temp ORDER BY id DESC LIMIT 20")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

		
		
if __name__ == '__main__':
    conn = create_connection("db_reg_temperature.db")
    select_all_data(conn)
	conn.close()
