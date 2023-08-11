#!/usr/bin/python3
"""Module to test the State class"""


import unittest
from unittest import mock
import os
import uuid
from io import StringIO
from time import sleep
from models.state import State
from models import storage
from datetime import datetime


class TestState_instantiation(unittest.TestCase):
    """Class to test State class instantiation"""

    def test_instantiation(self):
        """Method to test instantiation"""
        self.assertTrue(isinstance(State(), State))
        self.assertIn(State(), storage.all().values())

        self.assertTrue(isinstance(State().id, str))
        self.assertTrue(isinstance(State().created_at, datetime))
        self.assertTrue(isinstance(State().updated_at, datetime))

        self.assertEqual(str, type(State.name))

        with self.assertRaises(TypeError):
            State(None)

    def test_State_id(self):
        """method to test city id"""
        st = State()
        st2 = State()
        self.assertTrue(st.id != st2.id)
        uuid_st = uuid.UUID(st.id, version=4)
        uuid_st2 = uuid.UUID(st2.id, version=4)
        self.assertEqual(str(uuid_st), st.id)
        self.assertEqual(str(uuid_st2), st2.id)

    def test_state_created_at(self):
        """method to test state created time"""
        st = State()
        sleep(0.05)
        st2 = State()
        self.assertLess(st.created_at, st2.created_at)
        self.assertLess(st.updated_at, st2.updated_at)

    def test_state_string(self):
        """method to test state string representation"""
        st = State()
        st.name = 'Homabay Town'
        expected_output = st.__str__()
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(st, end="")
            actual_output = stdout.getvalue()
        self.assertEqual(actual_output, expected_output)


class TestState_to_dict(unittest.TestCase):
    """class to test dictionary representation of class State"""

    def test_to_dict(self):
        """method to test if to_dict returns a dictionary"""
        self.assertTrue(isinstance(State().to_dict(), dict))

    def test_to_dict_contains_keys(self):
        """method to test whether to_dict contains correct keys"""
        st = State()
        st.name = 'Kansas State'
        self.assertIn('id', st.to_dict())
        self.assertIn('created_at', st.to_dict())
        self.assertIn('updated_at', st.to_dict())
        self.assertIn('name', st.to_dict())
        self.assertIn('__class__', st.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """method to test for the added attributes"""
        st = State()
        st.area = 'Arujo'
        st.village = 'Sofia'
        self.assertIn('area', st.to_dict())
        self.assertIn('village', st.to_dict())

    def test_to_dict_output(self):
        """method to test for the to_dict output"""
        st = State()
        expected = str(st.to_dict())
        with mock.patch('sys.stdout', new=StringIO()) as stdout:
            print(str(st.to_dict()), end="")
            actual = stdout.getvalue()
        self.assertEqual(actual, expected)
        self.assertTrue(st.to_dict() != st.__dict__)

    def test_to_dict_with_arg(self):
        st = State()
        with self.assertRaises(TypeError):
            st.to_dict(None)


class TestState_save(unittest.TestCase):
    """class to test the save method for State class"""

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
        st = State()
        sleep(0.05)
        first_update = st.updated_at
        st.save()
        self.assertLess(first_update, st.updated_at)
        os.remove('file.json')

    def test_save_with_arg(self):
        """method to test save with arguments"""
        st = State()
        with self.assertRaises(TypeError):
            st.save(None)

    def test_save_updates_file(self):
        st = State()
        st.save()
        self.assertTrue(os.path.exists('file.json'))
        self.assertTrue(os.path.getsize('file.json') > 0)
        stid = 'State.' + st.id
        with open('file.json', 'r') as f:
            self.assertIn(stid, f.read())


if __name__ == '__main__':
    unittest.main()
