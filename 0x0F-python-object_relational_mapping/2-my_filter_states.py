#!/usr/bin/python3

"""
Script that takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    with MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306) as con:
        with con.cursor() as db_cursor:
            db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s "
                              "ORDER BY states.id", (sys.argv[4],))
            [print(record) for record in db_cursor.fetchall()]
