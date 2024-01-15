#!/usr/bin/python3

"""
Script that contains the class definition of a State and an
instance Base = declarative_base():
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    username, password, database = sys.argv[1:]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
