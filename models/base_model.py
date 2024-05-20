#!/usr/bin/python3
"""
Define a BaseModel class
"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Represents base model"""
    def __init__(self):
        """Initialize new BaseModel."""
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """Return string representation of the data"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Saving updated data"""
        updated_at = datetime.now().isoformat()

    def to_dict(self):
        """Return a dictionary representation of the data."""
        dict_rep = self.__dict__.copy()
        dict_rep['created_at'] = self.created_at
        dict_rep['updated_at'] = self.updated_at
        dict_rep['__class__'] = type(self).__name__

        return dict_rep
