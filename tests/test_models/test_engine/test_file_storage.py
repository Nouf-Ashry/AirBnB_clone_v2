#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up """
        delll = []
        for key in storage._FileStorage__objects.keys():
            delll.append(key)
        for key in delll:
            del storage._FileStorage__objects[key]

    def teDwn(self):
        """ Remove storage file """
        try:
            os.remove('file.json')
        except:
            pass

    def testListEmpty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def testNew(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def testAll(self):
        """ __objects is  returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def testBasemodelnsT(self):
        """ FiBaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def testEmpty(self):
        """ Data is saved to file """
        ne = BaseModel()
        thing = ne.to_dict()
        ne.save()
        ne2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def testSave(self):
        """ save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def testRload(self):
        """  """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def testReloadEmp(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def testREload(self):
        """  """
        self.assertEqual(storage.reload(), None)

    def testBasemodelSave(self):
        """ BaseModel save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def testTypePath(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def testTypeObj(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def testKeyFrmat(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def testStoCreated(self):
        """ FileStorage  created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)
