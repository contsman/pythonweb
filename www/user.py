from sqlalchemy import Column,INTEGER,Integer,String,DATE,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class User(object):
    __table__ = 'test'

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20))
    age = Column(String(20))