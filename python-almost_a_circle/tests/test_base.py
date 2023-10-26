#!/usr/bin/python3
"""Unit test for the Base class"""

import unittest
import os
from models.base import Base
import json


class TestBase(unittest.TestCase):
    """TestBase class to run tests"""

    def setUp(self):
        """Set up for each test method."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Tear down for each test method."""
        try:
            os.remove("Base.json")
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_id(self):
        """Test for id."""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)

    def test_to_json_string(self):
        """Test for `to_json_string` method."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = {"id": 12, "x": 0, "y": 0, "width": 3, "height": 4}
        json_str = Base.to_json_string([d])
        self.assertTrue(type(json_str) is str)
        self.assertEqual(json.loads(json_str), [d])

    def test_from_json_string(self):
        """Test for `from_json_string` method."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        d = {"id": 12, "x": 0, "y": 0, "width": 3, "height": 4}
        json_str = json.dumps([d])
        self.assertEqual(Base.from_json_string(json_str), [d])

    def test_save_to_file(self):
        """Test save_to_file method."""
        r = Base(3)
        Base.save_to_file([r])

        with open("Base.json", "r") as file:
            self.assertEqual([r.to_dictionary()], json.load(file))

    def test_create(self):
        """Test create method."""
        r = Base(3)
        r_dict = r.to_dictionary()
        r2 = Base.create(**r_dict)
        self.assertEqual(r.id, r2.id)
        self.assertNotEqual(r, r2)

    def test_load_from_file(self):
        """Test load_from_file method."""
        r = Base(3)
        Base.save_to_file([r])

        bases = Base.load_from_file()
        self.assertIsInstance(bases, list)
        self.assertIsInstance(bases[0], Base)
        self.assertEqual(bases[0].id, 3)


if __name__ == "__main__":
    unittest.main()
