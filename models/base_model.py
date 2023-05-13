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

    def __init__(self, **kwargs):
        """
        initializes BaseModel class
        """
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            ISO_fmt = '%Y-%m-%dT%H:%M:%S.%f'
            self.created_at = datetime.strptime(kwargs['created_at'], ISO_fmt)
            self.updated_at = datetime.strptime(kwargs['updated_at'], ISO_fmt)
            for key, value in kwargs.items():
                if key not in ('created_at', 'updated_at', '__class__'):
                    self.__dict__[key] = value



    def __str__(self):
        """
        Returns str representation of BaseModel

        [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {str(self.__dict__)}"

    def save(self):
        """
        Updates updated_at to current datetime
        """
        self.updated_at = datetime.now()
