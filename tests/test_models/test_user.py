#!/usr/bin/python3
"""Module to test the User Class module"""


import unittest
from unittest import mock
import os
from io import StringIO
import time
from models.user import User
from models import storage
from datetime import datetime


class TestUser(unittest.TestCase):
    """Class to test User class"""

    def test_instantiation(self):
        """Method to test instantiation"""
        self.assertEqual(type(User()), User)
        self.assertIn(User(), storage.all().values())

        self.assertTrue(isinstance(User().id, str))
        self.assertTrue(isinstance(User().created_at, datetime))
        self.assertTrue(isinstance(User().updated_at, datetime))

        self.assertEqual(str, type(User.email))
        self.assertEqual(str, type(User.password))
        self.assertEqual(str, type(User.first_name))
        self.assertEqual(str, type(User.last_name))

        with self.assertRaises(TypeError):
            User(None)

    def test_user_id(self):
        us1 = User()
        us2 = User()
        self.assertTrue(us1.id != us2.id)

    def test_user_time(self):
        us1 = User()
        time.sleep(0.05)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)
        self.assertLess(us1.updated_at, us2.updated_at)

    def test_user_string(self):
        us1 = User()
        us1.email = 'oloobrian89@gmail.com'
        expected_output = us1.__str__()
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(us1, end="")
            actual_output = stdout.getvalue()
        self.assertEqual(actual_output, expected_output)


class TestUser_save(unittest.TestCase):
    """method to test save method of the class"""

    @classmethod
    def setUp(self):
        if os.path.exists('file.json'):
            os.remove('file.json')

    @classmethod
    def tearDown(self):
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_save_one(self):
        us = User()
        time.sleep(0.05)
        first_update = us.updated_at
        us.save()
        self.assertLess(first_update, us.updated_at)

    def test_save_with_arg(self):
        us = User()
        with self.assertRaises(TypeError):
            us.save(None)

    def test_save_updates_file(self):
        us = User()
        us.save()
        self.assertTrue(os.path.exists('file.json'))
        self.assertTrue(os.path.getsize('file.json') > 0)
        usid = "User." + us.id
        with open("file.json", 'r') as f:
            self.assertIn(usid, f.read())


class TestSave_to_dict(unittest.TestCase):
    """Class to test the dictionary representation of User class"""

    def test_to_dict_type(self):
        self.assertTrue(isinstance(User().to_dict(), dict))

    def test_to_dict_contains_correct_keys(self):
        us = User()
        self.assertIn('id', us.to_dict())
        self.assertIn('created_at', us.to_dict())
        self.assertIn('updated_at', us.to_dict())
        self.assertIn("__class__", us.to_dict())

    def test_to_dict_contains_added_attribute(self):
        us = User()
        us.middle_name = 'Oloo'
        us.age = 29
        self.assertIn('Oloo', us.middle_name)
        self.assertIn('age', us.to_dict())

    def test_to_dict_output(self):
        us = User()
        expected = str(us.to_dict())
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(str(us.to_dict()), end="")
            actual = stdout.getvalue()
        self.assertEqual(actual, expected)

    def test_to_dict_dunder_dict(self):
        us = User()
        self.assertNotEqual(us.to_dict(), us.__dict__)

    def test_to_dict_with_arg(self):
        us = User()
        with self.assertRaises(TypeError):
            us.to_dict(None)


if __name__ == '__main__':
    unittest.main()
