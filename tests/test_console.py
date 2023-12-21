#!/usr/bin/python3
"""Unittest module for the console"""

import unittest
import os
import json
import pycodestyle
import io
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestCommand(unittest.TestCase):
    """Class tests console"""

    def setUp(self):
        """Function empties file.json"""
        FileStorage._FileStorage__objects = {}
        FileStorage().save()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Not FileStorage")
    def testCreate(self):
        """test the create"""
        storage = FileStorage()
        storage.reload()
        pt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        with self.assertRaises(AttributeError):
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("create BaseModel updated_at=0.0"
                                     " created_at=0.0")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create User email="jjk@wjj.nmk"'
                                 ' password="jkjkljlll"')
        res = f.getvalue().strip()
        self.assertRegex(res, pt)
        email = storage.all()[f'User.{res}'].email
        self.assertEqual(email, "jj@wjj.nmk")
        password = storage.all()[f'User.{res}'].password
        self.assertEqual(password, "jkjkljllll")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State johnny="bravo"'
                                 ' number="7" pi="3.14"')
        res = f.getvalue().strip()
        self.assertRegex(res, pt)
        johnny = storage.all()[f'State.{res}'].johnny
        self.assertEqual(johnny, "bravo")
        number = storage.all()[f'State.{res}'].number
        self.assertEqual(number, '7')
        pi = storage.all()[f'State.{res}'].pi
        self.assertEqual(pi, '3.14')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create City johnny="bravo" number="7"'
                                 ' pi="3.14"')
        res = f.getvalue().strip()
        self.assertRegex(res, pt)
        johnny = storage.all()[f'City.{res}'].johnny
        self.assertEqual(johnny, "bravo")
        number = storage.all()[f'City.{res}'].number
        self.assertEqual(number, '7')
        pi = storage.all()[f'City.{res}'].pi
        self.assertEqual(pi, '3.14')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create Amenity johnny="bravo"'
                                 ' number="7" pi="3.14"')
        res = f.getvalue().strip()
        self.assertRegex(res, pt)
        johnny = storage.all()[f'Amenity.{res}'].johnny
        self.assertEqual(johnny, "bravo")
        number = storage.all()[f'Amenity.{res}'].number
        self.assertEqual(number, '7')
        pi = storage.all()[f'Amenity.{res}'].pi
        self.assertEqual(pi, '3.14')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create Place johnny="bravo"'
                                 ' number="7" pi="3.14"')
        res = f.getvalue().strip()
        self.assertRegex(res, pt)
        johnny = storage.all()[f'Place.{res}'].johnny
        self.assertEqual(johnny, "bravo")
        number = storage.all()[f'Place.{res}'].number
        self.assertEqual(number, '7')
        pi = storage.all()[f'Place.{res}'].pi
        self.assertEqual(pi, '3.14')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create Review johnny="bravo"'
                                 ' number="7" pi="3.14"')
        res = f.getvalue().strip()
        self.assertRegex(res, pt)
        johnny = storage.all()[f'Review.{res}'].johnny
        self.assertEqual(johnny, "bravo")
        number = storage.all()[f'Review.{res}'].number
        self.assertEqual(number, '7')
        pi = storage.all()[f'Review.{res}'].pi
        self.assertEqual(pi, '3.14')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create')
        pt = '** class name missing **\n'
        self.assertEqual(f.getvalue(), pt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create NotClass')
        pt = '** class doesn\'t exist **\n'
        self.assertEqual(f.getvalue(), pt)

    def testPycodeStyle(self):
        """Pycodestyle test for console.py"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['console.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_console(self):
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)


if __name__ == '__main__':
    unittest.main()
