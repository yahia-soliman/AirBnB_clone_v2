#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, storage_is_db


class Amenity(BaseModel, Base):
    '''This is an Amenity Class'''
    name = ""

    if storage_is_db:
        from sqlalchemy import Column, String
        from sqlalchemy.orm import relationship
        from models.place import place_amenity
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity)
