#!/usr/bin/python3
"""Module to test the Review class module"""


import unittest
from unittest import mock
import os
import uuid
from io import StringIO
from time import sleep
from models.review import Review
from models.place import Place
from models.user import User
from models import storage
from datetime import datetime


class TestReview_instantiation(unittest.TestCase):
    """Class to test Review class instantiation"""

    def test_instantiation(self):
        """Method to test instantiation"""
        self.assertTrue(isinstance(Review(), Review))
        self.assertIn(Review(), storage.all().values())

        self.assertTrue(isinstance(Review().id, str))
        self.assertTrue(isinstance(Review().created_at, datetime))
        self.assertTrue(isinstance(Review().updated_at, datetime))

        self.assertEqual(str, type(Review.place_id))
        self.assertEqual(str, type(Review.user_id))
        self.assertEqual(str, type(Review.text))

        with self.assertRaises(TypeError):
            Review(None)

    def test_review_id(self):
        """method to test city id"""
        rv = Review()
        c2 = Review()
        self.assertTrue(rv.id != c2.id)
        uuid_c1 = uuid.UUID(rv.id, version=4)
        uuid_c2 = uuid.UUID(c2.id, version=4)
        self.assertEqual(str(uuid_c1), rv.id)
        self.assertEqual(str(uuid_c2), c2.id)

    def test_review_created_at(self):
        """method to test city created time"""
        rv = Review()
        sleep(0.05)
        c2 = Review()
        self.assertLess(rv.created_at, c2.created_at)
        self.assertLess(rv.updated_at, c2.updated_at)

    def test_review_string(self):
        """method to test city string representation"""
        rv = Review()
        rv.text = 'Homabay Town'
        expected_output = rv.__str__()
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(rv, end="")
            actual_output = stdout.getvalue()
        self.assertEqual(actual_output, expected_output)


class TestReview_to_dict(unittest.TestCase):
    """class to test dictionary representation of class Review"""

    def test_to_dict(self):
        """method to test if to_dict returns a dictionary"""
        self.assertTrue(isinstance(Review().to_dict(), dict))

    def test_to_dict_contains_keys(self):
        """method to test whether to_dict contains correct keys"""
        rv = Review()
        pl = Place()
        us = User()
        rv.place_id = str(pl.id)
        rv.user_id = str(us.id)
        rv.text = 'Kansas Review'
        self.assertIn('id', rv.to_dict())
        self.assertIn('created_at', rv.to_dict())
        self.assertIn('updated_at', rv.to_dict())
        self.assertIn('place_id', rv.to_dict())
        self.assertIn('user_id', rv.to_dict())
        self.assertIn('text', rv.to_dict())
        self.assertIn('__class__', rv.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """method to test for the added attributes"""
        rv = Review()
        rv.area = 'Arujo'
        rv.village = 'Sofia'
        self.assertIn('area', rv.to_dict())
        self.assertIn('village', rv.to_dict())

    def test_to_dict_output(self):
        """method to test for the to_dict output"""
        rv = Review()
        expected = str(rv.to_dict())
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(str(rv.to_dict()), end="")
            actual = stdout.getvalue()
        self.assertEqual(actual, expected)
        self.assertTrue(rv.to_dict() != rv.__dict__)

    def test_to_dict_with_arg(self):
        rv = Review()
        with self.assertRaises(TypeError):
            rv.to_dict(None)


class TestReview_save(unittest.TestCase):
    """class to test the save method for Review class"""

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
        rv = Review()
        sleep(0.05)
        first_update = rv.updated_at
        rv.save()
        self.assertLess(first_update, rv.updated_at)
        os.remove('file.json')

    def test_save_with_arg(self):
        """method to test save with arguments"""
        rv = Review()
        with self.assertRaises(TypeError):
            rv.save(None)

    def test_save_updates_file(self):
        rv = Review()
        rv.save()
        self.assertTrue(os.path.exists('file.json'))
        self.assertTrue(os.path.getsize('file.json') > 0)
        rvid = 'Review.' + rv.id
        with open('file.json', 'r') as f:
            self.assertIn(rvid, f.read())


if __name__ == '__main__':
    unittest.main()
