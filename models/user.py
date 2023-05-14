#!/usr/bin/python3
"""
User.py
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User inherits from BaseModel

    Attributes:
        email (str): Public class attribute - User's email
        password (str): Public class attribute - User's password
        first_name (str): Public class attribute - User's first name
        last_name (str): Public class attribute - User's last name
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """init method for User class

        Attributes:
            args (list): Arguments lists
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
