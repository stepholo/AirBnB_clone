#!/usr/bin/python3
"""Module to test parent class attributes
"""


import unittest
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """class to test the BaseModel parent class"""

    def test_id(self):
        """method to test the id of an class instance"""

        no_1 = BaseModel()
        no_1_id = no_1.id
        self.assertEqual(no_1.id, no_1_id)
        self.assertTrue(isinstance(no_1_id, str))

        no_2 = BaseModel()
        no_2_id = no_2.id
        self.assertEqual(no_2.id, no_2_id)
        self.assertTrue(isinstance(no_2_id, str))

        self.assertFalse(no_1 is no_2)
        self.assertFalse(no_1_id == no_2_id)

        uuid_obj_1 = uuid.UUID(no_1_id, version=4)
        self.assertEqual(str(uuid_obj_1), no_1_id)

        uuid_obj_2 = uuid.UUID(no_2_id, version=4)
        self.assertEqual(str(uuid_obj_2), no_2_id)
