#!/usr/bin/python3
""" Test module for the Database storage"""

import unittest
import pycodestyle
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    """ Clas TestDBStorag the database storage"""
    
    def testPYcodeStyle(self):
        """Test for  in DBStorage"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def testDocstring_DBStor(self):
        """Test for DBStorage"""
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)


if __name__ == "__main__":
    unittest.main()
