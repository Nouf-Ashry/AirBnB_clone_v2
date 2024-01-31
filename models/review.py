#!/usr/bin/python3
""" Review class """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Review(BaseModel):
    """class review.

    Attributes:
        place_id (str): empty string: it will be the Place.id.
        user_id (str):  empty string: it will be the User.id.
        text (str):  empty string.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
