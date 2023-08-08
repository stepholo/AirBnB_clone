#!/usr/bin/python3
"""Module to define parent class that all child class
    inherits from.
"""


import uuid
from datetime import datetime


class BaseModel:
    """Parent class BaseModel that defines attributes
        to be inherited by the child class.

        Attributes:
            id: instance identifier assigned by random uuid (uuid4())
            created_at: the current date and time when the instance was created
            updated_at: the current date and time when the instance is updated
            __str__: String representation of the isntance
            save: method to updated the attribute updated_at with current datetime
            to_dict: method to retun keys/values of __dict__ of the instance
    """
    def __init__(self, id=None):
        """class construct"""
        self.id = str(uuid.uuid4())
