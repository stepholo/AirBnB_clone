#!/usr/bin/python3
"""Module that define class FileStorage"""


import os
import json


class FileStorage:
    """Class Filestorage that serializes instances to JSON and
        deserializes JSON file to instances

        Private Class attributes:
            __file_path: String - path to the JSON file(file.json)
            __objects: dictionary - empty but will strore all objects by
                        <class name>.id
        Public instance methods:
            all: returns the dictionary __objects
            new: sets in __objects the obj with key <obj class name>.id
            save: serializes __objects to the JSON file(path: __file_path)
            reload: deserializes the JSON file to __objects
                    (only if the JSON file exists: otherwise do nothing.
                    If the file doesnt exist, no exeception should be raised
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """instance method that returns the dictionary __object"""

        return FileStorage.__objects

    def new(self, obj):
        """Sets in __object the obj with key
            Parameter:
                obj: object to set into a dict
        """
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""

        with open(FileStorage.__file_path, 'w') as json_file:
            o = {k: obj.to_dict() for k, obj in FileStorage.__objects.items()}
            json.dump(o, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as json_file:
                data = json.load(json_file)
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                for key, value in data.items():
                    cls_name, obj_id = key.split('.')
                    if cls_name == 'BaseModel':
                        cls = BaseModel
                    elif cls_name == 'User':
                        cls = User
                    elif cls_name == 'State':
                        cls = State
                    elif cls_name == 'City':
                        cls = City
                    elif cls_name == 'Amenity':
                        cls = Amenity
                    elif cls_name == 'Place':
                        cls = Place
                    elif cls_name == 'Review':
                        cls = Review
                    else:
                        cls = None
                    if cls:
                        FileStorage.__objects[key] = cls(**value)
        else:
            pass
