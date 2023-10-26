#!/usr/bin/python3
import unittest, json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseClass(unittest.TestCase):
    """Class to test Base class functionality"""

    def setUp(self):
        """Reset the class counter before each test"""
        Base._Base__nb_objects = 0

    def test_no_id_given(self):
        """Test without providing an id"""
        instance = Base()
        self.assertEqual(1, instance.id)

    def test_valid_id(self):
        """Test with a provided id"""
        instance = Base(60)
        self.assertEqual(60, instance.id)

    def test_zero_id(self):
        """Test with id of 0"""
        instance = Base(0)
        self.assertEqual(0, instance.id)

    def test_negative_id(self):
        """Test with a negative id"""
        instance = Base(-30)
        self.assertEqual(-30, instance.id)

    def test_string_as_id(self):
        """Test with string as id"""
        instance = Base("Alice")
        self.assertEqual("Alice", instance.id)

    def test_list_as_id(self):
        """Test with a list as id"""
        instance = Base([10, 20, 30])
        self.assertEqual([10, 20, 30], instance.id)

    def test_dict_as_id(self):
        """Test with a dictionary as id"""
        instance = Base({"id_val": 119})
        self.assertEqual({"id_val": 119}, instance.id)

    def test_tuple_as_id(self):
        """Test with tuple as id"""
        instance = Base((9,))
        self.assertEqual((9,), instance.id)

    def test_json_conversion_type(self):
        """Test type after json conversion"""
        sqr_instance = Square(2)
        json_data = sqr_instance.to_dictionary()
        json_str = Base.to_json_string([json_data])
        self.assertEqual(type(json_str), str)

    def test_json_conversion_content(self):
        """Test content after json conversion"""
        sqr_instance = Square(2, 0, 0, 719)
        json_data = sqr_instance.to_dictionary()
        json_str = Base.to_json_string([json_data])
        self.assertEqual(
            json.loads(json_str), [{"id": 719, "y": 0, "size": 2, "x": 0}]
        )

    def test_json_conversion_None(self):
        """Test json conversion with None"""
        sqr_instance = Square(2, 0, 0, 719)
        json_data = sqr_instance.to_dictionary()
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_json_conversion_empty(self):
        """Test json conversion with empty list"""
        sqr_instance = Square(2, 0, 0, 719)
        json_data = sqr_instance.to_dictionary()
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

if __name__ == '__main__':
    unittest.main()

