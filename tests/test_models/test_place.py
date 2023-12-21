#!/usr/bin/python3
""" Test module for place.py file. """

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Test class for place.py """

    def __init__(self, *args, **kwargs):
        """ test_Place class constructor"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def testCityId(self):
        """ Tests the city id """
        new = self.value()
        self.assertNotEqual(type(new.city_id), str)

    def testUserId(self):
        """ Tests the user id"""
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)

    def testName(self):
        """ Tests the name"""
        new = self.value()
        self.assertNotEqual(type(new.name), str)

    def testDesc(self):
        """ TEst the description """
        new = self.value()
        self.assertNotEqual(type(new.description), str)

    def testNumberOFroom(self):
        """ TEst the number of rooms"""
        new = self.value()
        self.assertNotEqual(type(new.number_rooms), int)

    def testNumberOFbathrooms(self):
        """ TEst number of bathrooms"""
        new = self.value()
        self.assertNotEqual(type(new.number_bathrooms), int)

    def testMAxGuest(self):
        """ Tests  maximum number guests"""
        new = self.value()
        self.assertNotEqual(type(new.max_guest), int)

    def testPriceNight(self):
        """ Tests price night """
        new = self.value()
        self.assertNotEqual(type(new.price_by_night), int)

    def testLAtitude(self):
        """ Tests the latitude of the location """
        new = self.value()
        self.assertNotEqual(type(new.latitude), float)

    def testLngitude(self):
        """ Tests longitude"""
        new = self.value()
        self.assertNotEqual(type(new.latitude), float)

    def testAmenyIds(self):
        """ Test  amenity id """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
