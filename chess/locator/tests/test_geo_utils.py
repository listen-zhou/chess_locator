"""
Test Geo utils for address verification and converting addresses
to lat, lon
"""

import unittest

from django.core.exceptions import ValidationError

from mock import patch
from mock import Mock
from mock import MagicMock
from pygeocoder import Geocoder

from locator import geo_utils

class GeoUtilsTest(unittest.TestCase):
    """
    Test geo_utils module
    """
    def test_get_lat_lon(self):
        """
        Test if get lat lon returns tuple of lat lons
        """
        geo_obj = MagicMock(return_value=[Mock(), None])
        geo_obj[0].coordinates = (37.0000, 120.0000)
        Geocoder.geocode = Mock(return_value=geo_obj)

        lat_lon = geo_utils.get_lat_lon('CA')
        self.assertEquals(lat_lon, (37.0000, 120.0000))

    def test_address_is_valid(self):
        """
        Test if address_is_valid returns true for valid address
        """
        Geocoder.geocode = Mock()
        Geocoder.geocode.valid_address = True
        valid = geo_utils.address_is_valid('9500 Gilman Dr., San Diego')
        self.assertEquals(valid, True)

    # def test_address_is_invalid(self):
    #     """
    #     Test if address_is_valid returns validation error for invalid address
    #     """
    #     Geocoder.geocode = Mock()
    #     Geocoder.geocode.valid_address = False
    #     address = '9500 Gilman Dr., San Diego'
    #     self.assertRaises(
    #         ValidationError, geo_utils.address_is_valid, address)