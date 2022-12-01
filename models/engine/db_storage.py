#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from sqlalchemy import create_engine
import os
from os import getenv

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """init the engine"""
        username = os.getenv('HBNB_MYSQL_USER')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        password = os.getenv('HBNB_MYSQL_PWD')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            username, host,password, database), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.engine)

    def all(self, cls=None):
        """Return dictionary"""
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        result = {}
        if cls is classes:
            objs = self.__session.query(classes[cls]).all()
            for obj in objs:
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                result[key] = obj
        elif cls is None:
            for clas in classes:
                query = self.__session.query(classes[clas]).all()
                for obj in query:
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    result[key] = obj
        return result

    def new(self, obj):
        """add new object"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """save database"""
        self.__session.commit()

    def delete(self, obj):
        """delete object"""
        if obj is not None:
            self.delete(obj)

    def reload(self):
        """reload database"""
        Base.metadata.create_all(self.__engine)
        Session_m = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session_m)
        self.__session = Session()


    def close(self):
        """Close the session"""
        self.__session.close()

