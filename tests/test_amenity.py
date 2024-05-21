#!/usr/bin/python3
"""
test cases for amenity class
"""

from models.base_model import BaseModel
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unit test suite for testing the Amenity class."""

    def setUp(self):
        """Set up test methods."""
        self.amenity = Amenity()
        self.amenity.name = "Pool"

    def test_instance(self):
        """Test the instantiation of the Amenity class."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """Test the attributes of the Amenity class."""
        self.assertEqual(self.amenity.name, "Pool")

    def test_attribute_types(self):
        """Test the type of the name attribute."""
        self.assertIsInstance(self.amenity.name, str)

    def test_empty_attributes(self):
        """Test that the name attribute is an empty string by default."""
        new_amenity = Amenity()
        self.assertEqual(new_amenity.name, "")


if __name__ == '__main__':
    unittest.main()
