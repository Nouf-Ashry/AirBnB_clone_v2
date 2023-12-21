#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def testPlaceId(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.place_id), str)

    def testUserId(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)

    def testTXT(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.text), str)
