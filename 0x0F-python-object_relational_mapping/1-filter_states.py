#!/usr/bin/python3

"""
Script that lists all states with a name starting with N (upper N)
"""

import MySQLdb
import sys

if __name__ == "__main__":
    with MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306) as con:
        with con.cursor() as db_cursor:
            db_cursor.execute("""SELECT * FROM states
                                WHERE name LIKE BINARY 'N%'
                                ORDER BY states.id""")
            [print(record) for record in db_cursor.fetchall()]
