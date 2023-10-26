#!/usr/bin/python3
import unittest, json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseClass(unittest.TestCase):

    def test_auto_id_increment(self):
        """Test automatic ID incrementation."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_with_value(self):
        """Test explicit ID value."""
        b3 = Base(150)
        self.assertEqual(b3.id, 150)

    def test_id_increment_after_value(self):
        """Test ID incrementation after explicit value."""
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_id_valid(self):
        """Testing a valid id."""
        b = Base(45)
        self.assertEqual(b.id, 45)

    def test_id_at_zero(self):
        """Testing an ID at zero."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative_value(self):
        """Testing a negative id."""
        b = Base(-15)
        self.assertEqual(b.id, -15)

    def test_id_as_string(self):
        """Testing ID as string."""
        b = Base("John")
        self.assertEqual(b.id, "John")

    def test_id_as_list(self):
        """Testing ID as list."""
        b = Base([2, 4, 6])
        self.assertEqual(b.id, [2, 4, 6])

    def test_id_as_dict(self):
        """Testing ID as dictionary."""
        b = Base({"id": 95})
        self.assertEqual(b.id, {"id": 95})

    def test_id_as_tuple(self):
        """Testing ID as tuple."""
        b = Base((5,))
        self.assertEqual(b.id, (5,))

    def test_json_conversion_type(self):
        """Testing JSON conversion type."""
        sq = Square(2)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_json_conversion_value(self):
        """Testing JSON conversion value."""
        sq = Square(2, 0, 0, 405)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string), [{"id": 405, "y": 0, "size": 2, "x": 0}])

    def test_json_conversion_with_None(self):
        """Testing JSON conversion with None."""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_json_conversion_with_empty_list(self):
        """Testing JSON conversion with an empty list."""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")


if __name__ == '__main__':
    unittest.main()

