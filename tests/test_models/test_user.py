#!/usr/bin/python3
"""Module to test the User Class module"""


import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Class to test User class"""

    def test_instantiation(self):
        """Method to test instantiation"""
        self.assertEqual(type(User()), User)

        with self.assertRaises(TypeError):
            User(None)

        self.assertEqual(str, type(User.email))
        self.assertEqual(str, type(User.password))
        self.assertEqual(str, type(User.first_name))
        self.assertEqual(str, type(User.last_name))



