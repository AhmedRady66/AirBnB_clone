#!/usr/bin/python3
"""class User that inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """Define state class
    Attributes:
        name (str): name of the state.
    """
    name = ""
