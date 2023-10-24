#!/usr/bin/python3
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):

    def test_id_assignment(self):
        """Test if ids are assigned correctly."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(100)
        self.assertEqual(b3.id, 100)

        b4 = Base()
        self.assertEqual(b4.id, 3)


if __name__ == "__main__":
    unittest.main()
