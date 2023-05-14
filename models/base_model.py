##!/usr/bin/python3

"""
Module base_model contains class BaseModel
"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """
     class BaseModel definition

     Attributes:
        id: str => unique UUID assigned to instance on creation
        created_at: datetime => timestamp of instance creation
        updated_at: datetime => timestamp of update made to instance

    Methods:
        __init__(self, **kwargs) => Constructor to initialize new instance
        __str__(self) => returns string representation of an instance
        save(self) => updates updated_at attribute
        to_dict(self) => return key/value dict representation of an instance
    """

    def __init__(self, *args, **kwargs):
        """
        initializes BaseModel class

        creates now instance only when kwargs is empty
        """
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
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
        save instance to JSON serialization
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns dictionary containing keys/values of __dict__ of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
