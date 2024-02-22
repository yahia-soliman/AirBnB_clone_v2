#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,

                      Column(String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),

                      Column(String(60), ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )



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

    # For DBStorage:
    reviews = relationship('Review', cascade='all, delete', backref='place')
    amenities = relationship('Amenity', cascade='all, delete',
                                backref='place_amenities',
                                secondary=place_amenity,
                                viewonly=False)

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

    @property
    def amenities(self):
        '''This method returns the list of Amenity instances'''
        pass

    @amenities.setter
    def amenities(self):
        '''This method handles append method for adding
        an Amenity.id to the attribute amenity_ids'''
        pass
