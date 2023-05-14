#!/usr/bin/python3
"""
place.py
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class inherits BaseModel

    Attributes:
        city_id (str): Public class attribute - Place's city_id
        user_id (str): Public class attribute - Place's user_id
        name (str): Public class attribute - Place's name
        description (str): Public class attribute - Place's description
        number_rooms (int): Public class attribute - Place's number_rooms
        number_bathrooms (int): Public class attribute - Place's
            number_bathrooms
        max_guest (str): Public class attribute - Place's max_guest
        price_by_night (str): Public class attribute - Place's price_by_night
        latitude (float): Public class attribute - Place's latitude
        longitude (float): Public class attribute - Place's longitude
        amenity_ids (list): Public class attribute - Place's amenity_ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """init method for Place class

        Attributes:
            args (list): Arguments list
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
