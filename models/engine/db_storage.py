#!/usr/bin/python3
"""The engine module that deals with the MySQL database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv

from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """class for incapsulating CRUD operations"""
    __engine = None
    __session = None

    def __init__(self):
        """initialize the storage engine"""
        db_URI = 'mysql+mysqldb://' +
                 getenv('HBNB_MYSQL_USER') + ':' +
                 getenv('HBNB_MYSQL_PWD') + '@' +
                 getenv('HBNB_MYSQL_HOST') + '/' +
                 getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(db_URI, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retrieve all rows of a table or just all rows"""
        all = {}
        if cls == None:
            qurey = self.__session.query(
                User, State, City, Amenity, Place, Review
            )
        else:
            query = self.__session.query(cls)

        for row in query.all():
            key = row.__name__ + row.id
            all[key] = row

    def new(self, obj):
        """Insert new instance into the database"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes instance to the database"""
        self.__session.commit()

    def delete(self, obj):
        """Delete an instance from the database"""
        self.__session.delete(obj)

    def reload(self):
        """load the database and map it to Python classes"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
