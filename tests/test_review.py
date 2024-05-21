#!/usr/bin/python3
"""
test cases for review class
"""

from models.base_model import BaseModel
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Unit test suite for testing the Review class."""

    def setUp(self):
        """Set up test methods."""
        self.review = Review()
        self.review.place_id = "Place_12345"
        self.review.user_id = "User_67890"
        self.review.text = "Great place with fantastic views."

    def test_instance(self):
        """Test the instantiation of the Review class."""
        self.assertIsInstance(self.review, Review)

    def test_inheritance(self):
        """Test if Review inherits from BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """Test the attributes of the Review class."""
        self.assertEqual(self.review.place_id, "Place_12345")
        self.assertEqual(self.review.user_id, "User_67890")
        self.assertEqual(self.review.text, "Great place with fantastic views.")

    def test_attribute_types(self):
        """Test the type of each attribute."""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_empty_attributes(self):
        """Test that attributes are empty strings by default."""
        new_review = Review()
        self.assertEqual(new_review.place_id, "")
        self.assertEqual(new_review.user_id, "")
        self.assertEqual(new_review.text, "")


if __name__ == '__main__':
    unittest.main()
