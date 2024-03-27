#!/usr/bin/python3
import sys
from sqlalchemy import create_engine, bindparam, select, exc
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

if len(sys.argv) != 5:
    print("Error: Please provide enough arguments.")
    exit(1)

username = sys.argv[1]
passwd = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, passwd, database))
Session = sessionmaker(bind=engine)
session = Session()

try:
    stmt = select(State.id).where(
            State.name == bindparam("state_name")
        )
    states = session.execute(stmt, {"state_name": state_name}).fetchall()
    if (states):
        for state in states:
            print("{}".format(state.id))
    else:
        print('Not found')
except exc.SQLAlchemyError as err:
    print('Err:', err)
engine.dispose()
