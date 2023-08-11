#!/usr/bin/python3
"""Module to test the Place class module"""


import unittest
from unittest import mock
import os
import uuid
from io import StringIO
from time import sleep
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
from models import storage
from datetime import datetime


class TestPlace_instantiation(unittest.TestCase):
    """Class to test Place class instantiation"""

    def test_instantiation(self):
        """Method to test instantiation"""
        self.assertTrue(isinstance(Place(), Place))
        self.assertIn(Place(), storage.all().values())

        self.assertTrue(isinstance(Place().id, str))
        self.assertTrue(isinstance(Place().created_at, datetime))
        self.assertTrue(isinstance(Place().updated_at, datetime))

        self.assertEqual(str, type(Place.city_id))
        self.assertEqual(str, type(Place.user_id))
        self.assertEqual(str, type(Place.name))
        self.assertEqual(str, type(Place.description))
        self.assertEqual(int, type(Place.number_rooms))
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertEqual(int, type(Place.max_guest))
        self.assertEqual(int, type(Place.price_by_night))
        self.assertEqual(float, type(Place.latitude))
        self.assertEqual(float, type(Place.longitude))
        self.assertEqual(list, type(Place.amenity_ids))

        with self.assertRaises(TypeError):
            Place(None)

    def test_place_id(self):
        """method to test place id"""
        pl = Place()
        c2 = Place()
        self.assertTrue(pl.id != c2.id)
        uuid_c1 = uuid.UUID(pl.id, version=4)
        uuid_c2 = uuid.UUID(c2.id, version=4)
        self.assertEqual(str(uuid_c1), pl.id)
        self.assertEqual(str(uuid_c2), c2.id)

    def test_place_created_at(self):
        """method to test place created time"""
        pl = Place()
        sleep(0.05)
        c2 = Place()
        self.assertLess(pl.created_at, c2.created_at)
        self.assertLess(pl.updated_at, c2.updated_at)

    def test_place_string(self):
        """method to test place string representation"""
        pl = Place()
        us = User()
        ct = City()
        pl.name = 'Homabay Town'
        pl.number_rooms = 7
        pl.user_id = str(us.id)
        pl.city_id = str(ct.id)
        expected_output = pl.__str__()
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(pl, end="")
            actual_output = stdout.getvalue()
        self.assertEqual(actual_output, expected_output)


class TestPlace_to_dict(unittest.TestCase):
    """class to test dictionary representation of class Place"""

    def test_to_dict(self):
        """method to test if to_dict returns a dictionary"""
        self.assertTrue(isinstance(Place().to_dict(), dict))

    def test_to_dict_contains_keys(self):
        """method to test whether to_dict contains correct keys"""
        pl = Place()
        ct = City()
        us = User()
        am = Amenity()
        pl.city_id = str(ct.id)
        pl.user_id = str(us.id)
        pl.name = "Twin Breeze"
        pl.description = "Where you get value for your money"
        pl.number_rooms = 10
        pl.number_bathrooms = 3
        pl.max_guest = 5
        pl.price_by_night = 40
        pl.longitude = 0.10234
        pl.latitude = 1.45769
        pl.amenity_ids = pl.amenity_ids.append(am.id)
        self.assertIn('id', pl.to_dict())
        self.assertIn('created_at', pl.to_dict())
        self.assertIn('updated_at', pl.to_dict())
        self.assertIn('city_id', pl.to_dict())
        self.assertIn('user_id', pl.to_dict())
        self.assertIn('name', pl.to_dict())
        self.assertIn('description', pl.to_dict())
        self.assertIn('number_rooms', pl.to_dict())
        self.assertIn('number_bathrooms', pl.to_dict())
        self.assertIn('max_guest', pl.to_dict())
        self.assertIn('price_by_night', pl.to_dict())
        self.assertIn('latitude', pl.to_dict())
        self.assertIn('longitude', pl.to_dict())
        self.assertIn('amenity_ids', pl.to_dict())
        self.assertIn('__class__', pl.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """method to test for the added attributes"""
        pl = Place()
        pl.area = 'Arujo'
        pl.village = 'Sofia'
        self.assertIn('area', pl.to_dict())
        self.assertIn('village', pl.to_dict())

    def test_to_dict_output(self):
        """method to test for the to_dict output"""
        pl = Place()
        expected = str(pl.to_dict())
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(str(pl.to_dict()), end="")
            actual = stdout.getvalue()
        self.assertEqual(actual, expected)
        self.assertTrue(pl.to_dict() != pl.__dict__)

    def test_to_dict_with_arg(self):
        pl = Place()
        with self.assertRaises(TypeError):
            pl.to_dict(None)


class TestPlace_save(unittest.TestCase):
    """class to test the save method for Place class"""

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
        pl = Place()
        sleep(0.05)
        first_update = pl.updated_at
        pl.save()
        self.assertLess(first_update, pl.updated_at)
        os.remove('file.json')

    def test_save_with_arg(self):
        """method to test save with arguments"""
        pl = Place()
        with self.assertRaises(TypeError):
            pl.save(None)

    def test_save_updates_file(self):
        pl = Place()
        pl.save()
        self.assertTrue(os.path.exists('file.json'))
        self.assertTrue(os.path.getsize('file.json') > 0)
        ctid = 'Place.' + pl.id
        with open('file.json', 'r') as f:
            self.assertIn(ctid, f.read())


if __name__ == '__main__':
    unittest.main()
