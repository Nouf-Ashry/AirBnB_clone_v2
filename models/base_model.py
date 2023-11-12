#!/usr/bin/python3
"""BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """class BaseModel that defines all common
       attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value attributes.
        """

        formter = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for ky, val in kwargs.items():
                if ky == "created_at" or ky == "updated_at":
                    self.__dict__[ky] = datetime.strptime(val, formter)
                else:
                    self.__dict__[ky] = val
        else:
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at
            with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
           __dict__ of the instance
           by using self.__dict__
           a key __class__ must be added to this dictionary with
           the class name of the object
        """
        ndict = self.__dict__.copy()
        ndict["created_at"] = self.created_at.isoformat()
        ndict["updated_at"] = self.updated_at.isoformat()
        ndict["__class__"] = self.__class__.__name__
        return ndict

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>
        """
        noc = self.__class__.__name__
        return "[{}] ({}) {}".format(noc, self.id, self.__dict__)
