#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def testFrstName(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.first_name), str)

    def testLstName(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.last_name), str)

    def testEmail(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.email), str)

    def testPass(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.password), str)
