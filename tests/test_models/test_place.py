#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import unittest
from os import getenv


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "not supported in this storage version")
    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "not supported in this storage version")
    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "not supported in this storage version")
    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "not supported in this storage version")
    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "not supported in this storage version")
    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "not supported in this storage version")
    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "not supported in this storage version")
    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "not supported in this storage version")
    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "not supported in this storage version")
    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "not supported in this storage version")
    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "not supported in this storage version")
    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)