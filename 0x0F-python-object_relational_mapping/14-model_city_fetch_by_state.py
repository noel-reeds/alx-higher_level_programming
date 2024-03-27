#!/usr/bin/python3
import sys
from sqlalchemy import create_engine, exc, select
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from model_city import City

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
    stmt = select(State.name, City.id, City.name).\
                select_from(State).\
                join(City, State.id == City.state_id)
    cities = session.execute(stmt)
    if (cities):
        for state_name, city_id, city_name in cities:
            print("{}: ({}) {}".format(state_name, city_id, city_name))
except exc.SQLAlchemyError as err:
    print('Err:', err)
engine.dispose()
