#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, storage_is_db


class State(BaseModel, Base):
    """ State class """
    name = ""
    if storage_is_db:
        from sqlalchemy import Column, String
        from sqlalchemy.orm import relationship
        __tablename__ = 'states'
        name = Column('name', String(128), nullable=False)
        cities = relationship('City', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """get all cities, in case of file storage"""
            from models import storage
            from models.city_model import City
            all = storage.all(City)
            return [city for city in all if city.state_id == self.id]
