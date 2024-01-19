#!/usr/bin/python3

"""
Script that contains the class definition of a State and an
instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    State class representing a state entity in the database.

    Attributes:
        __tablename__ (str): The name of the database table for
       the 'State' class.
       custom_id (int): An auto-generated, unique identifier for
       each state.
       custom_name (str): The name of the state, with a maximum
       length of 128 characters.

    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
