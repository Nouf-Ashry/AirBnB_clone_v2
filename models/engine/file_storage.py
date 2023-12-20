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
        objcn = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objcn, obj.id)] = obj

    def save(self):
        """serialize __objects to the JSON file __file_path."""
        dicter = FileStorage.__objects
        obdicter = {obj: dicter[obj].to_dict() for obj in dicter.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obdicter, f)

    def reload(self):
        """deserialize the JSON file __file_path
        to __objects. if the file doesn’t exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obdicter = json.load(f)
                for u in obdicter.values():
                    clname = u["__class__"]
                    del u["__class__"]
                    self.new(eval(clname)(**u))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ calls reload()
        """
        self.reload()
