#!/usr/bin/python3
""" base model class for AirBnB"""
from sqlalchemy.ext.declarative import declarative_base
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


class BaseModel:
    """class BaseModel that defines all common
       attributes/methods for other classes
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return a string
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
           __dict__ of the instance
           by using self.__dict__
           a key __class__ must be added to this dictionary with
           the class name of the object
        """
        ndict = dict(self.__dict__)
        ndict["__class__"] = str(type(self).__name__)
        ndict["created_at"] = self.created_at.isoformat()
        ndict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in ndict.keys():
            del ndict['_sa_instance_state']
        return ndict

    def delete(self):
        """ delete
        """
        models.storage.delete(self)
