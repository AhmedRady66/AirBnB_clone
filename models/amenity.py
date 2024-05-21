#!/usr/bin/python3
"""class User that inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Define amenity class
    Attributes:
        name (str): name of the amenity.
   """
    name = ""
