#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import (create_engine)
import os

class DBStorage:
    __engine = None
    __session = None
    __table_dict = {"City": City, "Place": Place, "Review": Review, "State": State, "User": User}

    def __init__(self):
        self.__engine = create_engine(
        f"mysql+mysqldb://{os.getenv('HBNB_MYSQL_USER')}:{os.getenv('HBNB_MYSQL_PWD')}@{os.getenv('HBNB_MYSQL_HOST')}/{os.getenv('HBNB_MYSQL_DB')}",
        pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == "test":
            self.__table__.drop()

    def all(self, cls=None):
        dict = {}
        if cls is None:
            for table in self.__table_dict:
                for obj in self.__session.query(self.__table_dict[table]):
                    dict[f"[{obj.__class__.__name__}] ({obj.id})"] = obj.to_dict()
        elif cls in self.__table_dict:
            for obj in self.__session.query(self.__table_dict[cls]):
                dict[f"[{obj.__class__.__name__}] ({obj.id})"] = obj.to_dict()
        return dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj):
        if obj is not None:
            self.delete(object)

    def reload(self):
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
        Base.metadata.create_all(self.__engine)

    def close(self):
        """Close the session"""
        self.session.close()

