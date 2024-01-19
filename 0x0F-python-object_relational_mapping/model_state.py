#!/usr/bin/python3


"""
Script that contains the class definition of a State and an
instance Base = declarative_base():
"""

import sys
from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
mymetadata = MetaData(bind=Base.metadata.bind)


class State(Base):
    """
    Class with an id and a name attribute of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Usage: {} <username> <password> <database>"
                 .format(sys.argv[0]))

    username, password, database = sys.argv[1:4]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}',
        pool_pre_ping=True
    )

    from model_state import OtherClass

    Base.metadata.create_all(engine)
