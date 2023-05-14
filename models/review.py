#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
review.py
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inherits BaseModel

    Attributes:
        place_id (str): Public class attribute - Review's place_id
        user_id (str): Public class attribute - Review's user_id
        text (str): Public class attribute - Review's text
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """init method Review class

        Attributes:
            args (list): Arguments lists
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
