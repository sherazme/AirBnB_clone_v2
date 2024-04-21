#!/usr/bin/python3
"""
FileStorage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes_arr = {
        "Amenity": Amenity, "BaseModel": BaseModel, "City": City,
        "Place": Place, "Review": Review, "State": State, "User": User
    }


class FileStorage:
    """serializes & deserializes instances to JSON file"""

    # path to the JSON file
    __file_path = "file.json"
    # store objects
    __objects = {}

    def all(self, cls=None):
        """returns dictionary"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets objects"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes objects"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes to objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes_arr[jo[key]
                                                    ["__class__"]](**jo[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method """
        self.reload()
