#!/usr/bin/python3
"""
State.py
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State inherits from BaseModel

    Attribute:
        name (str): Public class attribute - State's name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """init method for State class

        Attributes:
            args (list): Arguments list
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
