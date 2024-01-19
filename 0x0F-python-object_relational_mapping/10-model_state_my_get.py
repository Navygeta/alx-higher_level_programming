#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument from given database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def find_state_by_name(username, password, database, state_name):
    """Find and print the State object with the specified name."""
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).filter(State.name == (state_name,))

    try:
        print(instance[0].id)
    except IndexError:
        print("Not found")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(
            "Usage: {} <username> <password> <database> <state_name>"
            .format(sys.argv[0])
        )

    username, password, database, state_name = sys.argv[1:5]
    find_state_by_name(username, password, database, state_name)
