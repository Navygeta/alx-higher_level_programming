#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument from given db
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def add_and_print_state(username, password, database, new_state_name):
    """Add a new state to the database and print its ID."""
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name=new_state_name)
    session.add(new_state)
    session.commit()

    new_instance = session.query(State).filter_by(name=new_state_name).first()
    print(new_instance.id)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(
            "Usage: {} <username> <password> <database> <new_state_name>"
            .format(sys.argv[0])
        )

    username, password, database, new_state_name = sys.argv[1:5]
    add_and_print_state(username, password, database, new_state_name)
