#!/usr/bin/python3
""" unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instant
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instant(unittest.TestCase):
    """testing instant of the FileStorage class."""

    def test_FileStorage_instant_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorageInstant_withArg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_privateStr(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorageObjects_is_privateDict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storageInitializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        Bm = BaseModel()
        ser = User()
        at = State()
        ce = Place()
        ty = City()
        Amy = Amenity()
        rw = Review()
        models.storage.new(Bm)
        models.storage.new(ser)
        models.storage.new(at)
        models.storage.new(ce)
        models.storage.new(ty)
        models.storage.new(Amy)
        models.storage.new(rw)
        self.assertIn("BaseModel." + Bm.id, models.storage.all().keys())
        self.assertIn(Bm, models.storage.all().values())
        self.assertIn("User." + ser.id, models.storage.all().keys())
        self.assertIn(ser, models.storage.all().values())
        self.assertIn("State." + at.id, models.storage.all().keys())
        self.assertIn(at, models.storage.all().values())
        self.assertIn("Place." + ce.id, models.storage.all().keys())
        self.assertIn(ce, models.storage.all().values())
        self.assertIn("City." + ty.id, models.storage.all().keys())
        self.assertIn(ty, models.storage.all().values())
        self.assertIn("Amenity." + Amy.id, models.storage.all().keys())
        self.assertIn(Amy, models.storage.all().values())
        self.assertIn("Review." + rw.id, models.storage.all().keys())
        self.assertIn(rw, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        Bm = BaseModel()
        ser = User()
        at = State()
        ce = Place()
        ty = City()
        Amy = Amenity()
        rw = Review()
        models.storage.new(Bm)
        models.storage.new(ser)
        models.storage.new(at)
        models.storage.new(ce)
        models.storage.new(ty)
        models.storage.new(Amy)
        models.storage.new(rw)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + Bm.id, save_text)
            self.assertIn("User." + ser.id, save_text)
            self.assertIn("State." + at.id, save_text)
            self.assertIn("Place." + ce.id, save_text)
            self.assertIn("City." + ty.id, save_text)
            self.assertIn("Amenity." + Amy.id, save_text)
            self.assertIn("Review." + rw.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        Bm = BaseModel()
        ser = User()
        at = State()
        ce = Place()
        ty = City()
        Amy = Amenity()
        rw = Review()
        models.storage.new(Bm)
        models.storage.new(ser)
        models.storage.new(at)
        models.storage.new(ce)
        models.storage.new(ty)
        models.storage.new(Amy)
        models.storage.new(rw)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + Bm.id, objs)
        self.assertIn("User." + ser.id, objs)
        self.assertIn("State." + at.id, objs)
        self.assertIn("Place." + ce.id, objs)
        self.assertIn("City." + ty.id, objs)
        self.assertIn("Amenity." + Amy.id, objs)
        self.assertIn("Review." + rw.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
