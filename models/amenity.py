#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
amenity.py
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inherits BaseModel

    Attribute:
        name (str): Public class attribute - Amenity's name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """init method Amenity class

        Attributes:
            args (list): Argument list
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
