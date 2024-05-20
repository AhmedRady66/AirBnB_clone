#!/usr/bin/python3
"""class User that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Define Review class
    Attributes:
        place_id (str): Place id.
        user_id (str): User id.
        text (str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
