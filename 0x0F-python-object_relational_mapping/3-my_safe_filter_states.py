#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
But this time, the script is safe from MySQL injections!
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    match = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
