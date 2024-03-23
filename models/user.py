#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base, storage_is_db


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    if storage_is_db:
        from sqlalchemy import Column, String
        from sqlalchemy.orm import relationship
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', cascade='all, delete', backref='user')
        reviews = relationship('Review', cascade='all, delete', backref='user')
