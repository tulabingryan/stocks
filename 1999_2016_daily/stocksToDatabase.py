'''#############################################################
# Codes to create a unified SQL database for Philippine stock market data (daily 1999-2016)
# by: Ryan Tulabing
# Philippines Oct 2016
#############################################################'''


import sys
import os
import time
import datetime
import calendar
import csv
import numpy as np
import math
import sqlite3 as lite
import glob


def save_toDatabase(arrayToSave, databaseName):
    """ This function saves an array of data to an SQL database"""
    con = lite.connect(databaseName)
    with con:
        cur = con.cursor()
        #cur.execute('DROP TABLE IF EXISTS TMY')
        cur.execute('CREATE TABLE IF NOT EXISTS STOCKTABLE(SYMBOL,DATETIME, OPEN, HIGH, LOW, CLOSE, VOLUME, MISC)')
        cur.executemany('INSERT INTO STOCKTABLE VALUES(?,?,?,?,?,?,?,?)',arrayToSave)
    return


def process_csv(filename):
    '''
    This function reads data from a csv file and save them into a database
    '''
    with open(filename, 'rb') as f:
        data = csv.reader(f)
        arrayToSave = []
        for row in data:
            arrayToSave.append(row[:8])
        save_toDatabase(arrayToSave,'stocks.db')
    return 


def save_allToDatabase():
    """
    This function retrieves all data from all of the TMY csv files
    in the working folder and save them into one database
    """
    filenames = glob.glob('*.csv')
    for f in filenames:
        print 'Processing ', f, ' . . .'
        process_csv(f)
        print f, ' is save to the database'
    print 'Done saving all stocks data to database: stocks.db'
    return

if __name__ == '__main__':
    save_allToDatabase()
