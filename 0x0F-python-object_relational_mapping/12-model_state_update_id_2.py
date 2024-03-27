#!/usr/bin/python3
import sys
from sqlalchemy import create_engine, select, update, exc
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
    stmt = (
        update(State).
        where(State.id == 2).
        values(name='New Mexico')
    )
    session.execute(stmt)
    session.commit()
except exc.SQLAlchemyError as err:
    print('Err:', err)
engine.dispose()
