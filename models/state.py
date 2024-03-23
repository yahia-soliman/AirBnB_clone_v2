#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column('name', String(128), nullable=False)
    cities = relationship('City', cascade='all, delete-orphan')

    @property
    def cities(self):
        """get all cities, in case of file storage"""
        from models import storage
        from models.city_model import City
        all = storage.all(City)
        return [city for city in all if city.state_id == self.id]
