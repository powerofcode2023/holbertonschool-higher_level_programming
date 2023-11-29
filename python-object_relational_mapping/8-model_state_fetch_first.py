#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    record = session.query(State).first()
    if record is not None:
        print("{}: {}".format(record.id, record.name))
    else:
        print("Nothing")
