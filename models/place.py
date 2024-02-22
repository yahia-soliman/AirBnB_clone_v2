#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """

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
    amenity_ids = []

    # For DBStorage: class attribute reviews
    reviews = relationship('Review', cascade='all, delete', backref='place')

    # For FileStorage: getter attribute reviews
    @property
    def reviews(self):
        '''This method will returns the list of Review instances
        with place_id equals to the current Place.id
        '''
        review_list = []
        for rev in self.reviews:
            if rev.place_id == self.id:
                review_list.append(rev)

        return review_list
