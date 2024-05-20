#!/usr/bin/python3
"""
test cases for base_model class
"""

import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for BaseModel"""
    def test_initialization(self):
        self.assertIsInstance(BaseModel().id, str)
        self.assertTrue(BaseModel().id.startswith(''))
        self.assertNotEqual(BaseModel().created_at, BaseModel().updated_at)
        self.assertIsInstance(BaseModel().created_at, str)
        self.assertIsInstance(BaseModel().updated_at, str)
