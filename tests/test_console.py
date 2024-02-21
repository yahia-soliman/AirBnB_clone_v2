#!/usr/bin/python3
"""A module for testing a module that needs some tests"""
from io import StringIO 
from unittest import TestCase 
from unittest.mock import patch
from console import HBNBCommand
from models import storage


class test_HBNBCommand(TestCase):
    """Testing suite for the console"""
    def test_create(self):
        """testing the create method"""
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            HBNBCommand().onecmd('create Place name="Awl_Abbas" '
                                 'max_guest=5 longitude=12.42 '
                                 'user_id="I\\"m"')
            id = fake_out.getvalue()[:-1]
            place = storage._FileStorage__objects[f'Place.{id}']
            self.assertEqual(place.name, "Awl Abbas")
            self.assertEqual(place.max_guest, 5)
            self.assertEqual(place.longitude, 12.42)
            self.assertEqual(place.user_id, 'I"m')
