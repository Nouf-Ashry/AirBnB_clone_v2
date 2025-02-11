#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """class User.

    Attributes:
        email (str): empty string.
        password (str): empty string.
        first_name (str): empty string.
        last_name (str): empty string.
    """

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
