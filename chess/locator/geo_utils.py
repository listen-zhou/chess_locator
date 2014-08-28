"""
Geo utils for address verification and converting addresses
to lat, lon
"""

import logging

from django.core.exceptions import ValidationError

from pygeocoder import Geocoder
from pygeolib import GeocoderError


logger = logging.getLogger(__name__)


def get_lat_lon(address):
    """
    Get lat lon from address using pygeocoder

    :address:  Address to convert to lat lon
    :return:  Tuple of lat lon
    """
    results = Geocoder.geocode(address)
    return results[0].coordinates


def address_is_valid(address):
    """
    Validate address in the form of address, city.

    :address:  Address to validate, e.g. 9500 Gilman Dr., La Jolla
    :return:  True if valid, else False
    """
    #print "im in th efunction "
    try:
        valid = Geocoder.geocode(address).valid_address
        if valid:
            return True
        #logger.info('Im true')
        else:
            msg = "Not a valid address"
            raise ValidationError(msg)

    except GeocoderError:
        msg = "Google Maps/GeoCodeError.  Perhaps the address is invalid"
        raise ValidationError(msg)







