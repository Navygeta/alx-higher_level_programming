#!/usr/bin/python3


"""
Script that contains the class definition of a State and an
instance Base = declarative_base():
"""

import sys
from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

custom_metadata = MetaData()
Base = declarative_base(metadata=custom_metadata)

class State(Base):
    """
    State class representing a state entity in the database.

    Attributes:
        __tablename__ (str): The name of the database table for the 'State' class.
        id (int): An auto-generated, unique identifier for each state.
        name (str): The name of the state, with a maximum length of 128 characters.
    """
    __tablename__ = 'states'
    custom_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    custom_name = Column(String(128), nullable=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Usage: {} <custom_username> <custom_password> <custom_database>"
                 .format(sys.argv[0]))

    custom_username, custom_password, custom_database = sys.argv[1:4]
    custom_engine = create_engine(
        f'mysql+mysqldb://{custom_username}:{custom_password}@localhost/{custom_database}',
        pool_pre_ping=True
    )

    # Importing classes before calling create_all
    from model_state import OtherClass  # Add any other classes you have in model_state

    Base.metadata.create_all(custom_engine)

