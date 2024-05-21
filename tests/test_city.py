#!/usr/bin/python3
"""
test cases for city class
"""

from models.base_model import BaseModel
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Unit test suite for testing the City class."""

    def setUp(self):
        """Set up test methods."""
        self.city = City()
        self.city.name = "Cairo"
        self.city.state_id = "EG-01"

    def test_instance(self):
        """Test the instantiation of the City class."""
        self.assertIsInstance(self.city, City)

    def test_inheritance(self):
        """Test if City inherits from BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attribute_types(self):
        """Test attribute types of the City class"""
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)


if __name__ == '__main__':
    unittest.main()
