#!/usr/bin/python3
"""Module to define class City inherits from class BaseModel"""


from models.base_model import BaseModel


class City(BaseModel):
    """Class City
        Public Attribute:
            state_id: string - empty string: it will be the state.id
            name: empty string
    """
    state_id = ""
    name = ""
