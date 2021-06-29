#!/usr/bin/python3
"""

"""


import models
import json
import os


class FileStorage:
    __file_path = "BaseModel.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj == {} or obj is None:
            return
        key = obj["__class__"] + "." + obj["id"]
        FileStorage.__objects[key] = obj

    def save(self):
        if FileStorage.__objects is None or FileStorage.__objects == {}:
            pass
        my_dict = {}
        for k, v in self.__objects.items():
            my_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, mode="w") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r") as f:
                FileStorage.__objects = json.load(f)
        else:
            pass
