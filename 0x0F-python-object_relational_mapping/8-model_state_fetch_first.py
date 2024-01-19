#!/usr/bin/python3
"""
Script that prints the first State object from the given database.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_first_state(engine_url):
    """Prints the first State object from the specified database."""
    engine = create_engine(engine_url)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    with Session() as session:
        instance = session.query(State).first()

        if instance is None:
            print("Nothing")
        else:
            print(instance.id, instance.name, sep=": ")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Usage: {} <username> <password> <database>"
                 .format(sys.argv[0]))

    username, password, database = sys.argv[1:4]
    engUrl = f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'

    print_first_state(engUrl)
