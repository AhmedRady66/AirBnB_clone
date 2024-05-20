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

    def test_str(self):
        model = BaseModel()
        str_format = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(model.__str__(), str_format)

    def test_save(self):
        """Test the save method."""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)


if __name__ == '__main__':
    unittest.main()
