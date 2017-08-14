#!/usr/bin/python1
"""
Place Class from Models Module
"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey

class PlaceAmenity(BaseModel, Base):
    """ PlaceAmenity class """
    __tablename__ = 'place_amenity'
    metadata = Base.metadata
    place_id = Column(String(60), ForeignKey('places.id'), primary_key=True, nullable=False)
    amenity_id = Column(String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)

class Place(BaseModel, Base):
    """Place class handles all application places"""

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenities = relationship('Amenity', secondary='place_amenity', viewonly=False)
    reviews = relationship('Review', backref='place', cascade='delete')
    def __init__(self, *args, **kwargs):
        """instantiates a new place"""
        super().__init__(self, *args, **kwargs)
