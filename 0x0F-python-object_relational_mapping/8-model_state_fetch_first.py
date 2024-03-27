#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

if len(sys.argv) != 4:
    print("Error: Please provide enough arguments.")
    exit(1)

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

try:
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()
    if (state):
        print("{}: {}".format(state.id, state.name))
    else:
        print('Nothing')
except engine.Error as err:
    print("Error:", err)
engine.dispose()
