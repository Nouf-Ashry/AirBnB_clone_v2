#!/usr/bin/python3
""" FileStorage class """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import shlex


class FileStorage:
    """class

    Attributes:
        __file_path (str): path to the JSON file.
        __objects (dict): dictionary - empty but will store all objects
        by <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """return the dictionary __objects."""
        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dic)
        else:
            return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize __objects to the JSON file __file_path."""
        my_dictor = {}
        for key, value in self.__objects.items():
            my_dictor[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dictor, f)

    def reload(self):
        """deserialize the JSON file __file_path
        to __objects. if the file doesn't exists."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
<<<<<<< HEAD
    def delete(self, obj=None):
        """ delete obj from __objects if it's 
            inside - if obj is equal to None
=======

    def delete(self, obj=None):
        """ delete
>>>>>>> ca86d162df3c9cd724608a7da04c8fb91261c9f8
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ calls reload()
        """
        self.reload()
