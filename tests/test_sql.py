#!/usr/bin/pyhthon3
"""test  MySQL"""
import MySQLdb
import unittest
from unittest.mock import patch
import io
from console import HBNBCommand
from os import getenv
from models.engine.db_storage import DBStorage
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "Not DBStorage")
class TestMySQL(unittest.TestCase):
    """Test for the SQL database"""
    bnn = None
    bvr = None

    def Connection(self):
        """Connect to MySQLdb"""
        storage = DBStorage()
        storage.reload()
        self.bnn = MySQLdb.connect(getenv('HBNB_MYSQL_HOST'),
                                   getenv('HBNB_MYSQL_USER'),
                                   getenv('HBNB_MYSQL_PWD'),
                                   getenv('HBNB_MYSQL_DB'))
        self.bvr = self.bnn.cursor()

    def DisConnection(self):
        """Disconnect MySQLdb"""
        self.bvr.close()
        self.bnn.close()
        self.bnn = None
        self.bvr = None

    def test_createState(self):
        """Test create of a State"""
        self.connection()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
        self.bvr.execute("SELECT COUNT(*) FROM states")
        res = self.bvr.fetchone()[0]
        self.assertEqual(res, 1)
        self.DisConnection()

    def test_createCity(self):
        """Test create of a City"""
        self.connection()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'''create City state_id="{id}"
                                 name="San_Francisco"''')
        self.bvr.execute("SELECT COUNT(*) FROM cities")
        res = self.bvr.fetchone()[0]
        self.assertEqual(res, 1)
        self.DisConnection()


if __name__ == '__main__':
    unittest.main()
