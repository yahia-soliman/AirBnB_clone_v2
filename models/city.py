#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base, storage_is_db


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    name = ""
    state_id = ""

    if storage_is_db:
        from sqlalchemy import Column, String, ForeignKey
        from sqlalchemy.orm import relationship
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', cascade='all, delete', backref='cities')
        state = relationship('State', back_populates='cities', uselist=False)
