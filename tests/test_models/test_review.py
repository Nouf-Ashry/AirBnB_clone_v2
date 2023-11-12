#!/usr/bin/python3
"""unittests for models/review.py.

Unittest classes:
    TestReview_instant
    TestReview_save
    TestReview_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instant(unittest.TestCase):
    """ testing instant of the Review class."""

    def test_no_args_instant(self):
        self.assertEqual(Review, type(Review()))

    def test_newInstance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_publicString(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_publicDatetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_publicDatetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_publicClass_attribute(self):
        Amy = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(Review()))
        self.assertNotIn("place_id", Amy.__dict__)

    def test_reviews_uniqueIds(self):
        Amy = Review()
        Amy1 = Review()
        self.assertNotEqual(Amy.id, Amy1.id)

    def test_reviews_diffCreated_at(self):
        Amy = Review()
        sleep(0.05)
        Amy1 = Review()
        self.assertLess(Amy.created_at, Amy1.created_at)

    def test_reviews_diffUpdated_at(self):
        Amy = Review()
        sleep(0.05)
        Amy1 = Review()
        self.assertLess(Amy.updated_at, Amy1.updated_at)

    def test_stringRepresent(self):
        tm = datetime.today()
        tm_repr = repr(tm)
        Amy = Review()
        Amy.id = "123456"
        Amy.created_at = Amy.updated_at = tm
        Amystr = Amy.__str__()
        self.assertIn("[Review] (123456)", Amystr)
        self.assertIn("'id': '123456'", Amystr)
        self.assertIn("'created_at': " + tm_repr, Amystr)
        self.assertIn("'updated_at': " + tm_repr, Amystr)

    def test_argsUnused(self):
        Amy = Review(None)
        self.assertNotIn(None, Amy.__dict__.values())

    def test_instant_with_kwargs(self):
        """instant with kwargs test"""
        tm = datetime.today()
        tm_is_o = tm.isoformat()
        Amy = Review(id="345", created_at=tm_is_o, updated_at=tm_is_o)
        self.assertEqual(Amy.id, "345")
        self.assertEqual(Amy.created_at, tm)
        self.assertEqual(Amy.updated_at, tm)

    def test_instant_with_NoneKwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
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
        Amy = Review()
        sleep(0.05)
        frst_updated_at = Amy.updated_at
        Amy.save()
        self.assertLess(frst_updated_at, Amy.updated_at)

    def test_twoSaves(self):
        Amy = Review()
        sleep(0.05)
        frst_updated_at = Amy.updated_at
        Amy.save()
        sec_updated_at = Amy.updated_at
        self.assertLess(frst_updated_at, sec_updated_at)
        sleep(0.05)
        Amy.save()
        self.assertLess(sec_updated_at, Amy.updated_at)

    def test_save_withArg(self):
        Amy = Review()
        with self.assertRaises(TypeError):
            Amy.save(None)

    def test_save_updates_file(self):
        Amy = Review()
        Amy.save()
        Amyid = "Review." + Amy.id
        with open("file.json", "r") as f:
            self.assertIn(Amyid, f.read())


class TestReview_to_dict(unittest.TestCase):
    """ testing to_dict method """

    def test_to_dictType(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dictCorrect_keys(self):
        Amy = Review()
        self.assertIn("id", Amy.to_dict())
        self.assertIn("created_at", Amy.to_dict())
        self.assertIn("updated_at", Amy.to_dict())
        self.assertIn("__class__", Amy.to_dict())

    def test_to_dictAttributes(self):
        Amy = Review()
        Amy.middle_name = "Hafsa"
        Amy.my_number = 17
        self.assertEqual("Hafsa", Amy.middle_name)
        self.assertIn("my_number", Amy.to_dict())

    def test_to_dict_tm_attributes_strs(self):
        Amy = Review()
        Amy_dict = Amy.to_dict()
        self.assertEqual(str, type(Amy_dict["id"]))
        self.assertEqual(str, type(Amy_dict["created_at"]))
        self.assertEqual(str, type(Amy_dict["updated_at"]))

    def test_to_dictOutput(self):
        tm = datetime.today()
        Amy = Review()
        Amy.id = "1234556"
        Amy.created_at = Amy.updated_at = tm
        tydict = {
            'id': '1234556',
            '__class__': 'Review',
            'created_at': tm.isoformat(),
            'updated_at': tm.isoformat(),
        }
        self.assertDictEqual(Amy.to_dict(), tydict)

    def test_contrast_to_dict(self):
        Amy = Review()
        self.assertNotEqual(Amy.to_dict(), Amy.__dict__)

    def test_to_dict_withArg(self):
        Amy = Review()
        with self.assertRaises(TypeError):
            Amy.to_dict(None)


if __name__ == "__main__":
    unittest.main()
