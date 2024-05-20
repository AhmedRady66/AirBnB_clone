#!/usr/bin/python3
"""class User that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Define city class
    Attributes:
        name (str): name of the city.
        state_id (str): id of the state.
    """
    state_id = ""
    name = ""
