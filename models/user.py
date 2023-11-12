#!/usr/bin/python3
""" the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User.

    Attributes:
        email (str): empty string.
        password (str): empty string.
        first_name (str): empty string.
        last_name (str): empty string.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
