#!/usr/bin/python3
"""Module to test the City class module"""


import unittest
from unittest import mock
import os
import uuid
from io import StringIO
from time import sleep
from models.city import City
from models.state import State
from models import storage
from datetime import datetime


class TestCity_instantiation(unittest.TestCase):
    """Class to test City class instantiation"""

    def test_instantiation(self):
        """Method to test instantiation"""
        self.assertTrue(isinstance(City(), City))
        self.assertIn(City(), storage.all().values())

    def test_city_instances(self):
        """Method to test the instances types"""
        self.assertTrue(isinstance(City().id, str))
        self.assertTrue(isinstance(City().created_at, datetime))
        self.assertTrue(isinstance(City().updated_at, datetime))
        self.assertEqual(str, type(City.state_id))
        self.assertEqual(str, type(City.name))

    def test_instantiate_with_arg(self):
        """Method to test instantiation with argument"""
        with self.assertRaises(TypeError):
            City(None)

    def test_city_id(self):
        """method to test city id"""
        c1 = City()
        c2 = City()
        self.assertTrue(c1.id != c2.id)
        uuid_c1 = uuid.UUID(c1.id, version=4)
        uuid_c2 = uuid.UUID(c2.id, version=4)
        self.assertEqual(str(uuid_c1), c1.id)
        self.assertEqual(str(uuid_c2), c2.id)

    def test_city_created_at(self):
        """method to test city created time"""
        c1 = City()
        sleep(0.05)
        c2 = City()
        self.assertLess(c1.created_at, c2.created_at)
        self.assertLess(c1.updated_at, c2.updated_at)

    def test_city_string(self):
        """method to test city string representation"""
        c1 = City()
        c1.name = 'Homabay Town'
        expected_output = c1.__str__()
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(c1, end="")
            actual_output = stdout.getvalue()
        self.assertEqual(actual_output, expected_output)


class TestCity_to_dict(unittest.TestCase):
    """class to test dictionary representation of class City"""

    def test_to_dict(self):
        """method to test if to_dict returns a dictionary"""
        self.assertTrue(isinstance(City().to_dict(), dict))

    def test_to_dict_contains_keys(self):
        """method to test whether to_dict contains correct keys"""
        c1 = City()
        st = State()
        c1.state_id = str(st.id)
        c1.name = 'Kansas City'
        self.assertIn('id', c1.to_dict())
        self.assertIn('created_at', c1.to_dict())
        self.assertIn('updated_at', c1.to_dict())
        self.assertIn('state_id', c1.to_dict())
        self.assertIn('name', c1.to_dict())
        self.assertIn('__class__', c1.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """method to test for the added attributes"""
        c1 = City()
        c1.area = 'Arujo'
        c1.village = 'Sofia'
        self.assertIn('area', c1.to_dict())
        self.assertIn('village', c1.to_dict())

    def test_to_dict_output(self):
        """method to test for the to_dict output"""
        c1 = City()
        expected = str(c1.to_dict())
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(str(c1.to_dict()), end="")
            actual = stdout.getvalue()
        self.assertEqual(actual, expected)
        self.assertTrue(c1.to_dict() != c1.__dict__)

    def test_to_dict_with_arg(self):
        c1 = City()
        with self.assertRaises(TypeError):
            c1.to_dict(None)


class TestCity_save(unittest.TestCase):
    """class to test the save method for City class"""

    @classmethod
    def setUp(self):
        if os.path.exists('file.json'):
            os.remove('file.json')

    @classmethod
    def tearDown(self):
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_save(self):
        """method to test save for one"""
        c1 = City()
        sleep(0.05)
        first_update = c1.updated_at
        c1.save()
        self.assertLess(first_update, c1.updated_at)
        os.remove('file.json')

    def test_save_with_arg(self):
        """method to test save with arguments"""
        c1 = City()
        with self.assertRaises(TypeError):
            c1.save(None)

    def test_save_updates_file(self):
        c1 = City()
        c1.save()
        self.assertTrue(os.path.exists('file.json'))
        self.assertTrue(os.path.getsize('file.json') > 0)
        ctid = 'City.' + c1.id
        with open('file.json', 'r') as f:
            self.assertIn(ctid, f.read())


if __name__ == '__main__':
    unittest.main()
