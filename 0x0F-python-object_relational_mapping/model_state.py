#!/usr/bin/python3
"""
First state model
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, Sequence

Base = declarative_base()
engine = create_engine('mysql+mysqldb://:altoid:1234@localhost/3306/mydb')


class State(Base):
    """
    State class inherits from Base
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, Sequence('user_id_seq'), not None, doc="The primary key identifier for the state.")
    name = Column(String(128), not None, doc="The name of the state.")
