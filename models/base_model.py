##!/usr/bin/python3

"""
Module base_model contains class BaseModel
"""

import uuid
from datetime import datetime

class BaseModel():
    """
     class BaseModel definition

     Attributes:
    """

    def __init__(self):
        """
        initializes BaseModel class
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

