#!/usr/bin/python3
"""
Define FileStorage class
"""

from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.place import Place
# from models.amenity import Amenity
# from models.review import Review
from json import dump, load


class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): path to the JSON file .
        __objects (dict): dictionary will store all objects by <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return objects"""
        return FileStorage.__objects

    def new(self, obj):
        """set value of id to object"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        objdic = {}

        for key, value in FileStorage.__objects.items():
            objdic[key] = value.to_dict()
            with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
                dump(objdic, f)

    def reload(self):
        """deserializes the JSON file"""
        definedClasses = {'BaseModel': BaseModel}
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as fi:
                deserial = load(fi)

                for key, value in deserial.items():
                    clName = value["__class__"]
                    clobj = definedClasses[clName]

                    self.new(clobj(**value))

        except FileNotFoundError:
            pass
