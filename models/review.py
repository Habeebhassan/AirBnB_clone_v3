#!/usr/bin/python3
"""
Review class for the hbnb project
"""
import os
from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    """ A class representing a review in the HBNB project"""

    __tablename__ = 'reviews'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
