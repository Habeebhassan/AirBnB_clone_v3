#!/usr/bin/python3
"""
City class for hbnb project
"""
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """ A class representing a city in the HBNB project """

    __tablename__ = 'cities'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship(
            'Place',
            cascade='all, delete, delete-orphan',
            backref='cities'
        )
    else:
        name = ""
        state_id = ""
        places = None
