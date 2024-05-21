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
        """Test if state is instance from State"""
        self.assertIsInstance(self.state, State)

    def test_attribute_types(self):
        """Test attribute types of the State class"""
        self.assertIsInstance(self.state.name, str)


if __name__ == '__main__':
    unittest.main()
