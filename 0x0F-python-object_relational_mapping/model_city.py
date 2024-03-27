#!/usr/bin/python3
"""Second state model implemeted in SQLAlchemy."""
from model_state import Base, State
from sqlalchemy import *


class City(Base):
    """City class inherits from Base."""
    __tablename__ = 'cities'

    id = Column(
            Integer,
            unique=True,
            primary_key=True,
            nullable=False,
            autoincrement=True
     )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("State.id"), nullable=False)
