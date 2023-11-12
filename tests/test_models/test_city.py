#!/usr/bin/python3
"""unittests for models/city.py

Unittest classes:
    TestCity_instant
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instant(unittest.TestCase):
    """testing instantiation of the City class."""

    def test_no_args_instant(self):
        self.assertEqual(City, type(City()))

    def test_nInstance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_publicString(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_publicDatetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_publicDatetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_publicClass_attribute(self):
        ty = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(ty))
        self.assertNotIn("state_id", ty.__dict__)

    def test_name_is_pubClass_attribute(self):
        ty = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(ty))
        self.assertNotIn("name", ty.__dict__)

    def test_two_cities_uniqueIds(self):
        ty1 = City()
        ty2 = City()
        self.assertNotEqual(ty1.id, ty2.id)

    def test_two_cities_diffCreated_at(self):
        ty1 = City()
        sleep(0.05)
        ty2 = City()
        self.assertLess(ty1.created_at, ty2.created_at)

    def test_two_cities_diffUpdated_at(self):
        ty1 = City()
        sleep(0.05)
        ty2 = City()
        self.assertLess(ty1.updated_at, ty2.updated_at)

    def test_str_Rpres(self):
        tm = datetime.today()
        tm_repr = repr(tm)
        ty = City()
        ty.id = "123456"
        ty.created_at = ty.updated_at = tm
        tystr = ty.__str__()
        self.assertIn("[City] (123456)", tystr)
        self.assertIn("'id': '123456'", tystr)
        self.assertIn("'created_at': " + tm_repr, tystr)
        self.assertIn("'updated_at': " + tm_repr, tystr)

    def test_args_Unused(self):
        ty = City(None)
        self.assertNotIn(None, ty.__dict__.values())

    def test_instant_with_kwargs(self):
        tm = datetime.today()
        tm_iso = tm.isoformat()
        ty = City(id="345", created_at=tm_iso, updated_at=tm_iso)
        self.assertEqual(ty.id, "345")
        self.assertEqual(ty.created_at, tm)
        self.assertEqual(ty.updated_at, tm)

    def test_instant_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """testing save method of the City class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

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
        ty = City()
        sleep(0.05)
        first_updated_at = ty.updated_at
        ty.save()
        self.assertLess(first_updated_at, ty.updated_at)

    def test_twoSaves(self):
        ty = City()
        sleep(0.05)
        first_updated_at = ty.updated_at
        ty.save()
        second_updated_at = ty.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        ty.save()
        self.assertLess(second_updated_at, ty.updated_at)

    def testSave_with_arg(self):
        ty = City()
        with self.assertRaises(TypeError):
            ty.save(None)

    def test_saveUpdates_file(self):
        ty = City()
        ty.save()
        tyid = "City." + ty.id
        with open("file.json", "r") as f:
            self.assertIn(tyid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """testing to_dict method of the City class."""

    def test_to_dictType(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dictCorrect_keys(self):
        ty = City()
        self.assertIn("id", ty.to_dict())
        self.assertIn("created_at", ty.to_dict())
        self.assertIn("updated_at", ty.to_dict())
        self.assertIn("__class__", ty.to_dict())

    def test_to_dictAdded_attributes(self):
        ty = City()
        ty.middle_name = "Hafsa"
        ty.my_number = 98
        self.assertEqual("Hafsa", ty.middle_name)
        self.assertIn("my_number", ty.to_dict())

    def test_to_dict_datetime_Strings(self):
        ty = City()
        ty_dict = ty.to_dict()
        self.assertEqual(str, type(ty_dict["id"]))
        self.assertEqual(str, type(ty_dict["created_at"]))
        self.assertEqual(str, type(ty_dict["updated_at"]))

    def test_to_dictOutput(self):
        tm = datetime.today()
        ty = City()
        ty.id = "123456"
        ty.created_at = ty.updated_at = tm
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': tm.isoformat(),
            'updated_at': tm.isoformat(),
        }
        self.assertDictEqual(ty.to_dict(), tdict)

    def test_contrast_to_dict_duDict(self):
        ty = City()
        self.assertNotEqual(ty.to_dict(), ty.__dict__)

    def test_to_dictWith_arg(self):
        ty = City()
        with self.assertRaises(TypeError):
            ty.to_dict(None)


if __name__ == "__main__":
    unittest.main()
