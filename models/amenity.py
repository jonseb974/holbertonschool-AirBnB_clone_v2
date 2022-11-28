#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place_amenity

class Amenity(BaseModel, Base):
    __tablename__="amenities"
    name = Column(String(128), nullable=False)
    places = relationship("Place_amenity", back_populates="amenity")
