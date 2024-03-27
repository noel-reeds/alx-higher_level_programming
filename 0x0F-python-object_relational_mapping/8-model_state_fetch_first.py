#!/usr/bin/python3
"""Prints the first State object from the database"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://:{}:{}@localhost/3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).first()
    if (states):
        for state in states:
            print("{}: {}".format(state.id, state.name))
    else:
        print('Nothing)
