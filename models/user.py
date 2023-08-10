#!/usr/bin/python3
"""Module that defines class User and Inherits from BaseModel class"""


from models.base_model import BaseModel


class User(BaseModel):
    """Class User Inherits from  BaseModel Class
        Public class attribute:
            email: empty string
            password: empty string
            first_name: empty string
            last_name: empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
