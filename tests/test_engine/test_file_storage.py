#!/usr/bin/python3
"""Module to containing the test cases for FileStorage class"""


import unittest
import os
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing FileStorage class instantiation"""

    def test_FileStrorage_instantiation_no_args(self):
        """Method to test FileStorage instantiation"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instatiation_with_arg(self):
        """Method to test instatiation with argument"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """Method to test private class attribute"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_is_private_dict(self):
        """Method to test if FileStorage instance is private"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        """Method to test storage initialization"""
        self.assertEqual(type(storage), FileStorage)

    def test_private_attribute_file__objects(self):
        """method to test setting file__objects to none"""
        fs = FileStorage()
        fs._FileStorage__file_path = None
        self.assertEqual(type(None), type(fs._FileStorage__file_path))

    def test_private_attribute__objects(self):
        """method to test __object attribute"""
        fs = FileStorage()
        fs._FileStorage__objects = []
        self.assertEqual(list, type(fs._FileStorage__objects))


class TestFileStorage_methods(unittest.TestCase):
    """Class to test the methods of FileStorage class"""

    @classmethod
    def setUp(self):
        """set up class"""
        try:
            os.rename('file.json', 'tmp')
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """tear down class"""
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

    def test_all_type_return(self):
        """method to test whether all returns empty dict"""
        fs = FileStorage()
        dic = fs.all()
        self.assertEqual(dict, type(dic))
        self.assertTrue(len(dic) < 1)

    def test_all_with_arg(self):
        """method to test all method with argument"""
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self):
        """method to test the new method of FileStorage class"""
        obj = BaseModel()
        storage.new(obj)
        self.assertIn("BaseModel." + obj.id, storage.all().keys())
        self.assertIn(obj, storage.all().values())

        def test_new_invalid_argument(self):
            """method to test new() with invalid argument"""
            with self.assertRaises(TypeError):
                storage.new(BaseModel(), 'a')

        def test_new_with_none_argument(self):
            """method to test new() method with None argument"""
            with self.assertRaises(AttributeError):
                storage.new(None)

        def test_new_with_empty_argument(self):
            """method to test new with no argument"""
            fs = FileStorage()
            with self.assertRaises(AttributeError):
                sf = fs.new(fs)
            with self.assertRaises(TypeError):
                sf = fs.new()

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
        us = User()
        storage.new(bm)
        storage.new(us)
        storage.save()
        text = ''
        with open('file.json', 'r') as fd:
            text = fd.read()
            self.assertIn("BaseModel." + bm.id, text)
            self.assertIn("User." + us.id, text)

        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload(self):
        """method to test if deserialization is done properly"""
        if os.path.exists('file.json'):
            os.remove('file.json')
        bm = BaseModel()
        us = User()
        storage.save()
        storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertTrue(isinstance(obj, dict))
        self.assertIn("BaseModel." + bm.id, obj)
        self.assertIn("User." + us.id, obj)

        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == '__main__':
    unittest.main()
