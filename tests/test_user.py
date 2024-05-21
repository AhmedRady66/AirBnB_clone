#!/usr/bin/python3
"""
test cases for user class
"""

from models.base_model import BaseModel
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Unit test suite for testing the User class."""

    def setUp(self):
        """Set up test methods."""
        self.user = User()
        self.user.email = "user@example.com"
        self.user.password = "secure_password"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

    def test_instance(self):
        """Test the instantiation of the User class."""
        self.assertIsInstance(self.user, User)

    def test_inheritance(self):
        """Test if User inherits from BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """Test the attributes of the User class."""
        self.assertEqual(self.user.email, "user@example.com")
        self.assertEqual(self.user.password, "secure_password")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_attribute_types(self):
        """Test the type of each attribute."""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_empty_attributes(self):
        """Test that attributes are empty strings by default."""
        new_user = User()
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")


if __name__ == '__main__':
    unittest.main()
