#!/usr/bin/python3
"""Module to test the Amenity class"""


import unittest
from unittest import mock
import os
import uuid
from io import StringIO
from time import sleep
from models.amenity import Amenity
from models import storage
from datetime import datetime


class TestAmenity_instantiation(unittest.TestCase):
    """Class to test Amenity class inamantiation"""

    def test_instantiation(self):
        """Method to test inamantiation"""
        self.assertTrue(isinstance(Amenity(), Amenity))
        self.assertIn(Amenity(), storage.all().values())

        self.assertTrue(isinstance(Amenity().id, str))
        self.assertTrue(isinstance(Amenity().created_at, datetime))
        self.assertTrue(isinstance(Amenity().updated_at, datetime))

        self.assertEqual(str, type(Amenity.name))

        with self.assertRaises(TypeError):
            Amenity(None)

    def test_Amenity_id(self):
        """method to test city id"""
        am = Amenity()
        am2 = Amenity()
        self.assertTrue(am.id != am2.id)
        uuid_am = uuid.UUID(am.id, version=4)
        uuid_am2 = uuid.UUID(am2.id, version=4)
        self.assertEqual(str(uuid_am), am.id)
        self.assertEqual(str(uuid_am2), am2.id)

    def test_amate_created_at(self):
        """method to test amate created time"""
        am = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am.created_at, am2.created_at)
        self.assertLess(am.updated_at, am2.updated_at)

    def test_amenity_string(self):
        """method to test amate string representation"""
        am = Amenity()
        am.name = 'Homabay Town'
        expected_output = am.__str__()
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(am, end="")
            actual_output = stdout.getvalue()
        self.assertEqual(actual_output, expected_output)


class TestAmenity_to_dict(unittest.TestCase):
    """class to test dictionary representation of class Amenity"""

    def test_to_dict(self):
        """method to test if to_dict returns a dictionary"""
        self.assertTrue(isinstance(Amenity().to_dict(), dict))

    def test_to_dict_contains_keys(self):
        """method to test whether to_dict contains correct keys"""
        am = Amenity()
        am.name = 'Sub-hoofer'
        self.assertIn('id', am.to_dict())
        self.assertIn('created_at', am.to_dict())
        self.assertIn('updated_at', am.to_dict())
        self.assertIn('name', am.to_dict())
        self.assertIn('__class__', am.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """method to test for the added attributes"""
        am = Amenity()
        am.tv = 'Samsung Android 52`'
        am.wifi = 'Sofia.456'
        self.assertIn('tv', am.to_dict())
        self.assertIn('wifi', am.to_dict())

    def test_to_dict_output(self):
        """method to test for the to_dict output"""
        am = Amenity()
        expected = str(am.to_dict())
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(str(am.to_dict()), end="")
            actual = stdout.getvalue()
        self.assertEqual(actual, expected)
        self.assertTrue(am.to_dict() != am.__dict__)

    def test_to_dict_with_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)


class TestAmenity_save(unittest.TestCase):
    """class to test the save method for Amenity class"""

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
        am = Amenity()
        sleep(0.05)
        firam_update = am.updated_at
        am.save()
        self.assertLess(firam_update, am.updated_at)
        os.remove('file.json')

    def test_save_with_arg(self):
        """method to test save with arguments"""
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updates_file(self):
        am = Amenity()
        am.save()
        self.assertTrue(os.path.exists('file.json'))
        self.assertTrue(os.path.getsize('file.json') > 0)
        amid = 'Amenity.' + am.id
        with open('file.json', 'r') as f:
            self.assertIn(amid, f.read())


if __name__ == '__main__':
    unittest.main()
