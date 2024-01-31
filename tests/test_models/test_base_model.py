#!/usr/bin/python3
""" Module to test  the base model """

import os
import json
import unittest
import datetime
from models.base_model import BaseModel
from uuid import UUID


class test_basemodel(unittest.TestCase):
    """ Test  base model """

    def __init__(self, *args, **kwargs):
        """ test_basemodel class """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def setUp(self):
        """ """
        pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def testDef(self):
        """ """
        o = self.value()
        self.assertEqual(type(o), self.value)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def testKwags(self):
        """ """
        o = self.value()
        copy = o.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is o)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def testKwasInt(self):
        """ """
        o = self.value()
        copy = o.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def testSave(self):
        """ Test save """
        o = self.value()
        o.save()
        key = self.name + "." + o.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], o.to_dict())

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def testStr(self):
        """ """
        o = self.value()
        self.assertEqual(str(o), '[{}] ({}) {}'.format(self.name, o.id,
                         o.__dict__))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def testTodict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def testKwasNone(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def testKwasOne(self):
        """ """
        n = {'Name': 'test'}
        new = self.value(**n)
        self.assertRaises(KeyError)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def testId(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def testCreaAt(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def testUpdAt(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)


if __name__ == "__main__":
    unittest.main()
