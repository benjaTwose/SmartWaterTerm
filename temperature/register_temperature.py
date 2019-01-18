# -*- coding: utf-8 -*-
""" smart regulator for water term """

import sqlite3
from sqlite3 import Error
import datetime

def create_connection(db_file):
    """ create a db connection to sqlite db 
    :param db_file: database file
    :return: Connection object or None    
    """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        prinet(e)
    return none


def create_table(conn, create_table_sql):
    """ create table from the create table sql statement
    :param conn: connection to object
    :param create_table_sql: a CREATE TABLE SQL statement
    """
   
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e) 




def get_temp_sens(datafile):
    """ get temp sens, get temperature data from senor  
    :param datafile: path to file of sensor data
    
    """
    try:
        tfile = open(datafile)
        text = tfile.read()
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        # temperature = temperature / 1000   
        # return RAW data
        return float(temperature)
    
    except IOError as e:
        print (e)
        return None




def reg_temperature(conn,regdata):
    """ insert data into register
        :param conn: connection to object
        :param regdata: values for  INSERT  statement
    """

    sql_reg_temp = """ INSERT INTO reg_temp(date_reg,raw_temp) VALUES (?,?)   """

    try:
        c = conn.cursor()
        c.execute(sql_reg_temp, regdata)
        conn.commit()
        return c.lastrowid
    except Error as e:
        print(e)



def select_all_data(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM reg_temp ORDER BY id DESC LIMIT 10")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)



def main():
    database = 'db_reg_temperature.db'
    datafile = '/sys/bus/w1/devices/28-000006961afe/w1_slave'

    sql_create_temperatures_table = """ CREATE TABLE IF NOT EXISTS reg_temp (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        date_reg TEXT,
                                        raw_temp INTEGER
                                        ); """
    conn = create_connection(database)
    
    #read temperature from file
    temp = get_temp_sens(datafile)
    datatoreg =(datetime.datetime.now(),temp )
 
    if conn is not None:
        #create table
        create_table(conn, sql_create_temperatures_table)
        print(reg_temperature(conn,datatoreg))
    else:
        print("Error - cannot create the db connection")

    if temp is not None:
        msg = str(temp/1000) + " ºC"
        print(datetime.datetime.now())
        print(msg)
    

    select_all_data(conn)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()

