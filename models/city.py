#!/usr/bin/python3
"""
city.py
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class inherits BaseModel

    Attributes:
        name (str): Public class attribute - City's name
        state_id (str): Public class attribute - City's state_id
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """init method - City class

        Attributes:
            args (list): Arguments list
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
