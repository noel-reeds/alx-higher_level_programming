#!/usr/bin/python3
import sys
from sqlalchemy import create_engine, bindparam, select, exc
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

if len(sys.argv) != 4:
    print("Error: Please provide enough arguments.")
    exit(1)

username = sys.argv[1]
passwd = sys.argv[2]
database = sys.argv[3]

engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, passwd, database))
Session = sessionmaker(bind=engine)
session = Session()

try:
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    states = session.query(State.id).count()
    if (states):
        print("{}".format(states))
    else:
        print('Not found')
except exc.SQLAlchemyError as err:
    print('Err:', err)
engine.dispose()
