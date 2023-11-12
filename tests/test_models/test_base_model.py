#!/usr/bin/python3
"""unittests for models/base_model.py

Unittest classes:
    TestBaseModel_instant
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instant(unittest.TestCase):
    """testing instantiation of the BaseModel class."""

    def test_no_args_instant(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_newInstance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_publicString(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_publicDatetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_publicDatetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_models_uniqueIds(self):
        Bm = BaseModel()
        Bm1 = BaseModel()
        self.assertNotEqual(Bm.id, Bm1.id)

    def test_models_diffCreated_at(self):
        Bm = BaseModel()
        sleep(0.05)
        Bm1 = BaseModel()
        self.assertLess(Bm.created_at, Bm1.created_at)

    def test_models_diffUpdated_at(self):
        Bm = BaseModel()
        sleep(0.05)
        Bm1 = BaseModel()
        self.assertLess(Bm.updated_at, Bm1.updated_at)

    def test_strRepresent(self):
        tm = datetime.today()
        tm_repr = repr(tm)
        Bm = BaseModel()
        Bm.id = "123456"
        Bm.created_at = Bm.updated_at = tm
        Bmstr = Bm.__str__()
        self.assertIn("[BaseModel] (123456)", Bmstr)
        self.assertIn("'id': '123456'", Bmstr)
        self.assertIn("'created_at': " + tm_repr, Bmstr)
        self.assertIn("'updated_at': " + tm_repr, Bmstr)

    def test_args_unused(self):
        Bm = BaseModel(None)
        self.assertNotIn(None, Bm.__dict__.values())

    def test_instant_withKwargs(self):
        tm = datetime.today()
        tm_iso = tm.isoformat()
        Bm = BaseModel(id="345", created_at=tm_iso, updated_at=tm_iso)
        self.assertEqual(Bm.id, "345")
        self.assertEqual(Bm.created_at, tm)
        self.assertEqual(Bm.updated_at, tm)

    def test_instant_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instant_withArgs_and_kwargs(self):
        tm = datetime.today()
        tm_iso = tm.isoformat()
        Bm = BaseModel("12", id="345", created_at=tm_iso, updated_at=tm_iso)
        self.assertEqual(Bm.id, "345")
        self.assertEqual(Bm.created_at, tm)
        self.assertEqual(Bm.updated_at, tm)


class TestBaseModel_save(unittest.TestCase):
    """testing save method of the BaseModel class."""

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

    def test_oneSave(self):
        Bm = BaseModel()
        sleep(0.05)
        first_updated_at = Bm.updated_at
        Bm.save()
        self.assertLess(first_updated_at, Bm.updated_at)

    def test_twoSaves(self):
        Bm = BaseModel()
        sleep(0.05)
        first_updated_at = Bm.updated_at
        Bm.save()
        sec_updated_at = Bm.updated_at
        self.assertLess(first_updated_at, sec_updated_at)
        sleep(0.05)
        Bm.save()
        self.assertLess(sec_updated_at, Bm.updated_at)

    def test_saveWith_arg(self):
        Bm = BaseModel()
        with self.assertRaises(TypeError):
            Bm.save(None)

    def test_saveUpdates_file(self):
        Bm = BaseModel()
        Bm.save()
        Bmid = "BaseModel." + Bm.id
        with open("file.json", "r") as f:
            self.assertIn(Bmid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """testing to_dict method of the BaseModel class."""

    def test_to_dictType(self):
        Bm = BaseModel()
        self.assertTrue(dict, type(Bm.to_dict()))

    def test_to_dict_correct_keys(self):
        Bm = BaseModel()
        self.assertIn("id", Bm.to_dict())
        self.assertIn("created_at", Bm.to_dict())
        self.assertIn("updated_at", Bm.to_dict())
        self.assertIn("__class__", Bm.to_dict())

    def test_to_dict_addedAttributes(self):
        Bm = BaseModel()
        Bm.name = "Hafsa"
        Bm.my_number = 98
        self.assertIn("name", Bm.to_dict())
        self.assertIn("my_number", Bm.to_dict())

    def test_to_dictDatetime_attributes_are_strs(self):
        Bm = BaseModel()
        Bm_dict = Bm.to_dict()
        self.assertEqual(str, type(Bm_dict["created_at"]))
        self.assertEqual(str, type(Bm_dict["updated_at"]))

    def test_to_dict_output(self):
        tm = datetime.today()
        Bm = BaseModel()
        Bm.id = "123456"
        Bm.created_at = Bm.updated_at = tm
        tdct = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': tm.isoformat(),
            'updated_at': tm.isoformat()
        }
        self.assertDictEqual(Bm.to_dict(), tdct)

    def test_dictDunder_dict(self):
        Bm = BaseModel()
        self.assertNotEqual(Bm.to_dict(), Bm.__dict__)

    def test_to_dictWith_arg(self):
        Bm = BaseModel()
        with self.assertRaises(TypeError):
            Bm.to_dict(None)


if __name__ == "__main__":
    unittest.main()
