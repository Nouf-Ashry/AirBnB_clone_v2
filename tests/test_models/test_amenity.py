#!/usr/bin/python3
"""unittests for models/amenity.py

Unittest classes:
    TestAmenity_instant
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instant(unittest.TestCase):
    """ testing instant of the Amenity class."""

    def test_no_args_instant(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_newInstance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_publicString(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_publicDatetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_publicDatetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_publicClass_attribute(self):
        Amy = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", Amy.__dict__)

    def test_amenities_uniqueIds(self):
        Amy = Amenity()
        Amy1 = Amenity()
        self.assertNotEqual(Amy.id, Amy1.id)

    def test_amenities_diffCreated_at(self):
        Amy = Amenity()
        sleep(0.05)
        Amy1 = Amenity()
        self.assertLess(Amy.created_at, Amy1.created_at)

    def test_amenities_diffUpdated_at(self):
        Amy = Amenity()
        sleep(0.05)
        Amy1 = Amenity()
        self.assertLess(Amy.updated_at, Amy1.updated_at)

    def test_stringRepresent(self):
        tm = datetime.today()
        tm_repr = repr(tm)
        Amy = Amenity()
        Amy.id = "123456"
        Amy.created_at = Amy.updated_at = tm
        Amystr = Amy.__str__()
        self.assertIn("[Amenity] (123456)", Amystr)
        self.assertIn("'id': '123456'", Amystr)
        self.assertIn("'created_at': " + tm_repr, Amystr)
        self.assertIn("'updated_at': " + tm_repr, Amystr)

    def test_argsUnused(self):
        Amy = Amenity(None)
        self.assertNotIn(None, Amy.__dict__.values())

    def test_instant_with_kwargs(self):
        """instant with kwargs test"""
        tm = datetime.today()
        tm_is_o = tm.isoformat()
        Amy = Amenity(id="345", created_at=tm_is_o, updated_at=tm_is_o)
        self.assertEqual(Amy.id, "345")
        self.assertEqual(Amy.created_at, tm)
        self.assertEqual(Amy.updated_at, tm)

    def test_instant_with_NoneKwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """testing save"""

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
        Amy = Amenity()
        sleep(0.05)
        frst_updated_at = Amy.updated_at
        Amy.save()
        self.assertLess(frst_updated_at, Amy.updated_at)

    def test_twoSaves(self):
        Amy = Amenity()
        sleep(0.05)
        frst_updated_at = Amy.updated_at
        Amy.save()
        sec_updated_at = Amy.updated_at
        self.assertLess(frst_updated_at, sec_updated_at)
        sleep(0.05)
        Amy.save()
        self.assertLess(sec_updated_at, Amy.updated_at)

    def test_save_withArg(self):
        Amy = Amenity()
        with self.assertRaises(TypeError):
            Amy.save(None)

    def test_saveUpdates_file(self):
        Amy = Amenity()
        Amy.save()
        Amyid = "Amenity." + Amy.id
        with open("file.json", "r") as f:
            self.assertIn(Amyid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """ testing to_dict method """

    def test_to_dictType(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dictCorrect_keys(self):
        Amy = Amenity()
        self.assertIn("id", Amy.to_dict())
        self.assertIn("created_at", Amy.to_dict())
        self.assertIn("updated_at", Amy.to_dict())
        self.assertIn("__class__", Amy.to_dict())

    def test_to_dictAttributes(self):
        Amy = Amenity()
        Amy.middle_name = "Hafsa"
        Amy.my_number = 17
        self.assertEqual("Hafsa", Amy.middle_name)
        self.assertIn("my_number", Amy.to_dict())

    def test_to_dict_tm_attributes_strs(self):
        Amy = Amenity()
        Amy_dict = Amy.to_dict()
        self.assertEqual(str, type(Amy_dict["id"]))
        self.assertEqual(str, type(Amy_dict["created_at"]))
        self.assertEqual(str, type(Amy_dict["updated_at"]))

    def test_to_dictOutput(self):
        tm = datetime.today()
        Amy = Amenity()
        Amy.id = "1234556"
        Amy.created_at = Amy.updated_at = tm
        tydict = {
            'id': '1234556',
            '__class__': 'Amenity',
            'created_at': tm.isoformat(),
            'updated_at': tm.isoformat(),
        }
        self.assertDictEqual(Amy.to_dict(), tydict)

    def test_contrast_to_dict(self):
        Amy = Amenity()
        self.assertNotEqual(Amy.to_dict(), Amy.__dict__)

    def test_to_dict_withArg(self):
        Amy = Amenity()
        with self.assertRaises(TypeError):
            Amy.to_dict(None)


if __name__ == "__main__":
    unittest.main()
