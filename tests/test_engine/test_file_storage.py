#!/usr/bin/python3
"""Module to containing the test cases for FileStorage class"""


import unittest
import os
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing FileStorage class instantiation"""

    def test_FileStrorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instatiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Class to test the methods of FileStorage class"""

    @classmethod
    def setUp(self):
        try:
            os.rename('file.json', 'tmp')
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove('file.json')
        except IOError:
            pass
        try:
            os.rename('tmp', 'file.json')
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """method to test the all method"""
        self.assertEqual(dict, type(storage.all()))

        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self):
        """method to test the new method of FileStorage class"""
        obj = BaseModel()
        storage.new(obj)
        self.assertIn("BaseModel." + obj.id, storage.all().keys())
        self.assertIn(obj, storage.all().values())

        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 'a')

        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_save(self):
        """method to test if serializationis done properly"""

        if os.path.exists('file.json'):
            os.remove('file.json')
        obj = BaseModel()
        obj.Name = "Brian"
        obj.Age = 29
        obj.School = "Alx-Africa"
        storage.new(obj)
        storage.save()
        self.assertTrue(os.path.exists('file.json'))
        self.assertTrue(os.path.getsize('file.json') > 0)
        tet = ''
        with open('file.json', 'r') as fd:
            tet = fd.read()
            self.assertIn("BaseModel." + obj.id, tet)

        os.remove('file.json')
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        text = ''
        with open('file.json', 'r') as fd:
            text = fd.read()
            self.assertIn("BaseModel." + bm.id, text)

        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload(self):
        """method to test if deserialization is done properly"""
        if os.path.exists('file.json'):
            os.remove('file.json')
        bm = BaseModel()
        storage.save()
        storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertTrue(isinstance(obj, dict))
        self.assertIn("BaseModel." + bm.id, obj)

        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == '__main__':
    unittest.main()
