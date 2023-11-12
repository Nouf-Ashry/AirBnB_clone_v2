#!/usr/bin/python3
"""unittests for models/user.py

Unittest classes:
    TestUser_instant
    TestUser_save
    TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instant(unittest.TestCase):
    """ testing instant of the User class."""

    def test_no_args_instant(self):
        self.assertEqual(User, type(User()))

    def test_newInstance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_publicString(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_publicDatetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_publicDatetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_publicStr(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_publicStr(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_publicStr(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_publicStr(self):
        self.assertEqual(str, type(User.last_name))

    def test_users_uniqueIds(self):
        Amy = User()
        Amy1 = User()
        self.assertNotEqual(Amy.id, Amy1.id)

    def test_users_diffCreated_at(self):
        Amy = User()
        sleep(0.05)
        Amy1 = User()
        self.assertLess(Amy.created_at, Amy1.created_at)

    def test_users_diffUpdated_at(self):
        Amy = User()
        sleep(0.05)
        Amy1 = User()
        self.assertLess(Amy.updated_at, Amy1.updated_at)

    def test_stringRepresent(self):
        tm = datetime.today()
        tm_repr = repr(tm)
        Amy = User()
        Amy.id = "123456"
        Amy.created_at = Amy.updated_at = tm
        Amystr = Amy.__str__()
        self.assertIn("[User] (123456)", Amystr)
        self.assertIn("'id': '123456'", Amystr)
        self.assertIn("'created_at': " + tm_repr, Amystr)
        self.assertIn("'updated_at': " + tm_repr, Amystr)

    def test_argsUnused(self):
        Amy = User(None)
        self.assertNotIn(None, Amy.__dict__.values())

    def test_instant_with_kwargs(self):
        """instant with kwargs test"""
        tm = datetime.today()
        tm_is_o = tm.isoformat()
        Amy = User(id="345", created_at=tm_is_o, updated_at=tm_is_o)
        self.assertEqual(Amy.id, "345")
        self.assertEqual(Amy.created_at, tm)
        self.assertEqual(Amy.updated_at, tm)

    def test_instant_with_NoneKwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
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
        Amy = User()
        sleep(0.05)
        frst_updated_at = Amy.updated_at
        Amy.save()
        self.assertLess(frst_updated_at, Amy.updated_at)

    def test_twoSaves(self):
        Amy = User()
        sleep(0.05)
        frst_updated_at = Amy.updated_at
        Amy.save()
        sec_updated_at = Amy.updated_at
        self.assertLess(frst_updated_at, sec_updated_at)
        sleep(0.05)
        Amy.save()
        self.assertLess(sec_updated_at, Amy.updated_at)

    def test_save_withArg(self):
        Amy = User()
        with self.assertRaises(TypeError):
            Amy.save(None)

    def test_save_updates_file(self):
        Amy = User()
        Amy.save()
        Amyid = "User." + Amy.id
        with open("file.json", "r") as f:
            self.assertIn(Amyid, f.read())


class TestUser_to_dict(unittest.TestCase):
    """ testing to_dict method """

    def test_to_dictType(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dictCorrect_keys(self):
        Amy = User()
        self.assertIn("id", Amy.to_dict())
        self.assertIn("created_at", Amy.to_dict())
        self.assertIn("updated_at", Amy.to_dict())
        self.assertIn("__class__", Amy.to_dict())

    def test_to_dictAttributes(self):
        Amy = User()
        Amy.middle_name = "Hafsa"
        Amy.my_number = 17
        self.assertEqual("Hafsa", Amy.middle_name)
        self.assertIn("my_number", Amy.to_dict())

    def test_to_dict_tm_attributes_strs(self):
        Amy = User()
        Amy_dict = Amy.to_dict()
        self.assertEqual(str, type(Amy_dict["id"]))
        self.assertEqual(str, type(Amy_dict["created_at"]))
        self.assertEqual(str, type(Amy_dict["updated_at"]))

    def test_to_dictOutput(self):
        tm = datetime.today()
        Amy = User()
        Amy.id = "1234556"
        Amy.created_at = Amy.updated_at = tm
        tydict = {
            'id': '1234556',
            '__class__': 'User',
            'created_at': tm.isoformat(),
            'updated_at': tm.isoformat(),
        }
        self.assertDictEqual(Amy.to_dict(), tydict)

    def test_contrast_to_dict(self):
        Amy = User()
        self.assertNotEqual(Amy.to_dict(), Amy.__dict__)

    def test_to_dict_withArg(self):
        Amy = User()
        with self.assertRaises(TypeError):
            Amy.to_dict(None)


if __name__ == "__main__":
    unittest.main()
