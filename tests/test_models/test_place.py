#!/usr/bin/python3
"""unittests for models/place.py

Unittest classes:
    TestPlace_instant
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instant(unittest.TestCase):
    """testing instantiation of the Place class."""

    def test_no_args_instant(self):
        self.assertEqual(Place, type(Place()))

    def test_newInstance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_publicString(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_publicDatetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_publicDatetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_publicCLS(self):
        cr = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(cr))
        self.assertNotIn("city_id", cr.__dict__)

    def test_user_id_is_publicCLS(self):
        cr = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(cr))
        self.assertNotIn("user_id", cr.__dict__)

    def test_name_is_publicCLS(self):
        cr = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(cr))
        self.assertNotIn("name", cr.__dict__)

    def test_description_is_publiCLS(self):
        cr = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(cr))
        self.assertNotIn("desctiption", cr.__dict__)

    def test_number_rooms_is_publiCLAS(self):
        cr = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(cr))
        self.assertNotIn("number_rooms", cr.__dict__)

    def test_number_bathrooms_is_publicClass(self):
        cr = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(cr))
        self.assertNotIn("number_bathrooms", cr.__dict__)

    def test_max_guest_is_publicClas(self):
        cr = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(cr))
        self.assertNotIn("max_guest", cr.__dict__)

    def test_price_by_night_is_publicClass(self):
        cr = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(cr))
        self.assertNotIn("price_by_night", cr.__dict__)

    def test_latitude_is_publicClass(self):
        cr = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(cr))
        self.assertNotIn("latitude", cr.__dict__)

    def test_longitude_is_publiCLS(self):
        cr = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(cr))
        self.assertNotIn("longitude", cr.__dict__)

    def test_amenity_ids_is_publicClass(self):
        cr = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(cr))
        self.assertNotIn("amenity_ids", cr.__dict__)

    def test_two_Places_Ids(self):
        cr1 = Place()
        cr2 = Place()
        self.assertNotEqual(cr1.id, cr2.id)

    def test_two_Places_diffCreated_at(self):
        cr1 = Place()
        sleep(0.05)
        cr2 = Place()
        self.assertLess(cr1.created_at, cr2.created_at)

    def test_two_Places_diffUpdated_at(self):
        cr1 = Place()
        sleep(0.05)
        cr2 = Place()
        self.assertLess(cr1.updated_at, cr2.updated_at)

    def test_strRepresent(self):
        tm = datetime.today()
        tm_repr = repr(tm)
        cr = Place()
        cr.id = "123456"
        cr.created_at = cr.updated_at = tm
        crstr = cr.__str__()
        self.assertIn("[Place] (123456)", crstr)
        self.assertIn("'id': '123456'", crstr)
        self.assertIn("'created_at': " + tm_repr, crstr)
        self.assertIn("'updated_at': " + tm_repr, crstr)

    def test_argsUnused(self):
        cr = Place(None)
        self.assertNotIn(None, cr.__dict__.values())


class TestPlace_save(unittest.TestCase):
    """testing save method of the Place class."""

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
        Bm = Place()
        sleep(0.05)
        first_updated_at = Bm.updated_at
        Bm.save()
        self.assertLess(first_updated_at, Bm.updated_at)

    def test_twoSaves(self):
        Bm = Place()
        sleep(0.05)
        first_updated_at = Bm.updated_at
        Bm.save()
        sec_updated_at = Bm.updated_at
        self.assertLess(first_updated_at, sec_updated_at)
        sleep(0.05)
        Bm.save()
        self.assertLess(sec_updated_at, Bm.updated_at)

    def test_saveWith_arg(self):
        Bm = Place()
        with self.assertRaises(TypeError):
            Bm.save(None)

    def test_saveUpdates_file(self):
        Bm = Place()
        Bm.save()
        Bmid = "Place." + Bm.id
        with open("file.json", "r") as f:
            self.assertIn(Bmid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """testing to_dict method of the Place class."""

    def test_to_dictType(self):
        Bm = Place()
        self.assertTrue(dict, type(Bm.to_dict()))

    def test_to_dictCorrect_keys(self):
        Bm = Place()
        self.assertIn("id", Bm.to_dict())
        self.assertIn("created_at", Bm.to_dict())
        self.assertIn("updated_at", Bm.to_dict())
        self.assertIn("__class__", Bm.to_dict())

    def test_to_dict_Added_attributes(self):
        Bm = Place()
        Bm.name = "Hafsa"
        Bm.my_number = 98
        self.assertIn("name", Bm.to_dict())
        self.assertIn("my_number", Bm.to_dict())

    def test_to_dict_datetime_Stringss(self):
        Bm = Place()
        Bm_dict = Bm.to_dict()
        self.assertEqual(str, type(Bm_dict["created_at"]))
        self.assertEqual(str, type(Bm_dict["updated_at"]))

    def test_to_dictOutput(self):
        tm = datetime.today()
        Bm = Place()
        Bm.id = "123456"
        Bm.created_at = Bm.updated_at = tm
        xdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': tm.isoformat(),
            'updated_at': tm.isoformat()
        }
        self.assertDictEqual(Bm.to_dict(), xdict)

    def test_contrast_to_dict(self):
        Bm = Place()
        self.assertNotEqual(Bm.to_dict(), Bm.__dict__)

    def test_to_dictWith_arg(self):
        Bm = Place()
        with self.assertRaises(TypeError):
            Bm.to_dict(None)


if __name__ == "__main__":
    unittest.main()
