#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """Get a list of all related cities objects"""
        city_list = []
        villes = models.storage.all(City)
        for key, value in villes.items():
            if value.state_id == self.id:
                city_list.append(value)
        return city_list
