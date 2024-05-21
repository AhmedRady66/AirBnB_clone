#!/usr/bin/python3
"""
test cases for state class
"""

from models.base_model import BaseModel
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Unit test suite for testing the State class."""

    def setUp(self):
        """Set up test methods."""
        self.state = State()
        self.state.name = "Alexandria"

    def test_inheritance(self):
        """Test if State inherits from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_isinstance(self):
        """Test if state is an instance of State."""
        self.assertIsInstance(self.state, State)

    def test_attribute_types(self):
        """Test attribute types of the State class."""
        self.assertIsInstance(self.state.name, str)

    def test_name_attribute(self):
        """Test the name attribute of State."""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "Alexandria")

    def test_missing_attribute(self):
        """Test that attributes are set correctly even if missing."""
        del self.state.name
        self.assertTrue(hasattr(self.state, 'name'))
        self.state.name = "Cairo"
        self.assertEqual(self.state.name, "Cairo")


if __name__ == '__main__':
    unittest.main()
