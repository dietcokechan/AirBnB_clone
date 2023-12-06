#!/usr/bin/python3
"""serializes instances to a JSON file/deserializes JSON file to instances"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage(BaseModel):
    """definition"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """adds new object to objects"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize objects to json file"""
        jsonData = {}
        for key, value, in self.__objects.items():
            jsonData[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(jsonData, f)

    def reload(self):
        """deserialize json file to objects"""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj in data.items():
                    new = eval(obj['__class__'])(**obj)
                    self.__objects[key] = new
        except FileNotFoundError:
            pass
