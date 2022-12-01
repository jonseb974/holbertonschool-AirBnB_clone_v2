#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity

class DBStorage:
    """Represent a database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """init the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                    format(getenv('HBNB_MYSQL_USER'),
                           getenv('HBNB_MYSQL_HOST'),
                           getenv('HBNB_MYSQL_DB'),
                           getenv('HBNB_MYSQL_PWD')),
                        pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.engine)

    def all(self, cls=None):
        """Return dictionary"""
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())

        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__,o.id):o for o in objs}

    def new(self, obj):
        """add new object"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """save database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload database"""
        Base.metadata.create_all(self.__engine)
        Session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session_factory)
        self.__session = Session()

    def close(self):
        """Close the session"""
        self.__session.close()
