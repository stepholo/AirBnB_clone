#!/usr/bin/python3
"""Module to test parent class attributes
"""


import unittest
from unittest import mock
import uuid
from datetime import datetime
from io import StringIO
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """class to test the BaseModel parent class"""

    def test_id(self):
        """method to test the id attribute of a class instance"""

        no_1 = BaseModel()
        no_1_id = no_1.id
        self.assertEqual(no_1.id, no_1_id)
        self.assertTrue(isinstance(no_1_id, str))
        no_1.id = 10
        self.assertEqual(no_1.id, 10)

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

    def test_created_at(self):
        """Method to test the created_at attribute of an instance"""

        date_1 = BaseModel()
        base_date = date_1.created_at
        self.assertEqual(date_1.created_at, base_date)
        self.assertTrue(isinstance(base_date, datetime))

        expected_output = str(date_1.created_at)
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(date_1.created_at, end='')
            actual_output = stdout.getvalue()
        self.assertEqual(actual_output, expected_output)

    def test_updated_at(self):
        """Method to test the updated_at attribute of an instance"""

        date_2 = BaseModel()
        base_date = date_2.updated_at
        self.assertEqual(date_2.updated_at, base_date)
        self.assertTrue(isinstance(base_date, datetime))

        expected_output = str(date_2.updated_at)
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(date_2.updated_at, end='')
            actual_output = stdout.getvalue()
        self.assertEqual(actual_output, expected_output)

    def test_arguments(self):
        """Method to test the key word argument"""

        obj = BaseModel()
        obj.name = 'Brian'
        obj.age = 29
        obj.school = 'Alx-Africa'
        obj.save()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)

        self.assertFalse(obj is new_obj)
        expected_output = str(new_obj.to_dict())
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(new_obj.to_dict(), end='')
            actual_output = stdout.getvalue()
        self.assertEqual(actual_output, expected_output)

        with self.assertRaises(TypeError):
            new_obj = BaseModel(
                    '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                    '2017-09-28T21:03:54.052298',
                    '2017-09-28T21:03:54.052302'
                    )
            new_obj.id

        with self.assertRaises(AttributeError):
            new_obj = BaseModel(
                    d=10, created='2017-09-28T21:03:54.052302',
                    updated='2017-09-28T21:03:54.052302'
                    )
            print(new_obj)

        with self.assertRaises(KeyError):
            new_obj = BaseModel(
                    d=10, created='2017-09-28T21:03:54.052302',
                    updated='2017-09-28T21:03:54.052302'
                    )
            new_obj.to_dict()

    def test__str__(self):
        """Method to test the string representation of an object"""

        obj = BaseModel()
        obj.name = "Stephen Oloo"
        obj.number = 100
        expected_output = f"[BaseModel] ({obj.id}) {str(obj.__dict__)}"
        self.assertTrue(isinstance(expected_output, str))
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(obj, end='')
            actual_output = stdout.getvalue()
        self.maxDiff = None
        self.assertEqual(actual_output, expected_output)

    def test_save(self):
        """Method to test the save method of an object"""

        obj = BaseModel()
        obj_t1 = obj.created_at
        obj.save()
        obj_t2 = obj.updated_at
        self.assertFalse(obj_t1 == obj_t2)

    def test_to_dict(self):
        """Method to test the dictionary representation of the object"""

        obj = BaseModel()
        obj.name = 'Stephen Oloo'
        obj.age = 29
        obj.school = 'Alx Africa'
        obj_dict = obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))

        expected_output = str(obj_dict)
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(obj_dict, end='')
            actual_output = stdout.getvalue()
        self.maxDiff = None
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
