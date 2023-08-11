#!/usr/bin/python3
"""Module to define class Amenity"""


from models.base_models import BaseModel


class Amenity(BaseModel):
    """Class Amenity that inherits from BaseModel
        Public Attribute:
            name: empty string
    """
    name = ""
