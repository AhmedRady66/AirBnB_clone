#!/usr/bin/python3
"""
Define a BaseModel class
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents base model"""
    def __init__(self, *args, **kwargs):
        """Initialize new BaseModel."""
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    dictime = datetime.fromisoformat(value)
                    setattr(self, key, dictime)
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()
            from models import storage
            storage.new(self)

    def __str__(self):
        """Return string representation of the data"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Saving updated data"""
        from models import storage
        self.updated_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the data."""
        dictFormat = {}
        dictFormat["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                dictFormat[key] = val.isoformat()
            else:
                dictFormat[key] = val
        return dictFormat
