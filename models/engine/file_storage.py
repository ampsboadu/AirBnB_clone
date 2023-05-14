#!/usr/bin/python3
"""
module file_storage contains class FileStorage
"""

import json
from os import path


class FileStorage():
    """
    class FileStorage definition

    Attributes:
        __file_path: str => string path to JSON file
        __objects: dict => dictionary to store all objects
    Methods:
    """

    __file_path = "file.json"
    __objects = dict()

    def __init__(self):
        """
        Initiazes new instances
        """
        pass

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects
