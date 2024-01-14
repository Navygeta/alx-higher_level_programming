#!/usr/bin/python3

"""
Script that takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    with MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306) as db:
        with db.cursor() as cur:
            cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s",
                        (sys.argv[4] + '%',))

            [print(row) for row in cur.fetchall()]
