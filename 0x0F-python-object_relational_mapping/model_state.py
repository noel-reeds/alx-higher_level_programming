#!/usr/bin/python3
"""
First state model
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, Sequence

if __name__ == "__main__":
    Base = declarative_base()
    engine = create_engine('mysql+mysqldb://:altoid:1234@localhost/3306/mydb')


    class State(Base):
        """
        State class inherits from Base
        """
        __tablename__ = 'states'

        id = Column(
                Integer,
                Sequence('user_id_seq'),
                primary_key=True,
                nullable=False
         )
        name = Column(String(128), nullable=False)
