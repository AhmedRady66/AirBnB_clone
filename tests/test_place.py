#!/usr/bin/python3
"""
test cases for city class
"""

from models.base_model import BaseModel
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unit test suite for testing the Place class."""

    def setUp(self):
        """Set up test methods."""
        self.place = Place()
        self.place.city_id = "Cairo-123"
        self.place.user_id = "User-456"
        self.place.name = "Sunny Retreat"
        self.place.description = "A cozy place with a beautiful view of the Nile."
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 4
        self.place.price_by_night = 150
        self.place.latitude = 30.0444
        self.place.longitude = 31.2357
        self.place.amenity_ids = ["Pool", "WiFi", "Air Conditioning"]

    def test_instance(self):
        """Test the instantiation of the Place class."""
        self.assertIsInstance(self.place, Place)

    def test_inheritance(self):
        """Test if Place inherits from BaseModel."""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        """Test the attributes of the Place class."""
        self.assertEqual(self.place.city_id, "Cairo-123")
        self.assertEqual(self.place.user_id, "User-456")
        self.assertEqual(self.place.name, "Sunny Retreat")
        self.assertEqual(self.place.description, "A cozy place with a beautiful view of the Nile.")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 150)
        self.assertAlmostEqual(self.place.latitude, 30.0444)
        self.assertAlmostEqual(self.place.longitude, 31.2357)
        self.assertListEqual(self.place.amenity_ids, ["Pool", "WiFi", "Air Conditioning"])

    def test_attribute_types(self):
        """Test the type of each attribute."""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

if __name__ == '__main__':
    unittest.main()
