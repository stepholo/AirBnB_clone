#!/usr/bin/python3
"""Module to define class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Child class Review inherits form BaseModel
        Public class attributes
            place_id: empty string: it will be the Place.id
            user_id: empty string: it will be the User.id
            text: empty string
    """
    place_id = ""
    user_id = ""
    text: ""
