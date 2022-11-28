#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

class Place_amenity(Base):
    __tablename__ = 'place_amenity'
    place_id = Column(ForeignKey('places.id'), primary_key=True)
    amenity_id = Column(ForeignKey('amenities.id'), primary_key=True)
    amenity = relationship("Amenity", back_populates="places")
    place = relationship("Place", back_populates="amenities")


class Place(BaseModel, Base):
    """
        Describes the places of the hbnb
    """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))

    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)

    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)

    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    amenity_ids = []

    city = relationship("City", back_populates="places")
    user = relationship("User", back_populates="places")
    amenities = relationship("Place_amenity", back_populates="place")


City.places = relationship(
    "Place", order_by=Place.id, back_populates="city")
User.places = relationship(
    "Place", order_by=Place.id, back_populates="user")


