"""
Module for validators and decorators 
"""

import os

# import logging
from abc import ABC, abstractmethod

from awdible.logger import logger


class Validator(ABC):
    """Abstract class for validators"""

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass
