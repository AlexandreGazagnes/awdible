"""
Module for validators and decorators 
"""

import os
from awdible.logger import logger

# import logging
from abc import ABC, abstractmethod


from awdible.core.defaults import DEFAULT_CONFIG


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


class Number(Validator):
    """Validator for numbers"""

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"Expected {self.private_name[1:]} to be an int or float : received {type(value)} for {value}"
            )


class Crop(Validator):
    """Validator for numbers"""

    MIN = 0
    MAX = 3_600 * 10

    def validate(self, value):
        if not isinstance(value, (int, float, str)):
            raise TypeError(
                f"Expected {self.private_name[1:]} to be an int or float  or str: received {type(value)} for {value}"
            )

        try:
            value = int(value)
        except Exception as e:
            raise ValueError(
                f"Expected {self.private_name[1:]} to be an int : received {type(value)} for {value} : {e}"
            )

        if value < self.MIN or value > self.MAX:
            raise ValueError(
                f"Expected {self.private_name[1:]} to be between {self.MIN} and {self.MAX} : received {value}"
            )


class Bool(Validator):
    """Validator for bools"""

    def validate(self, value):
        if not isinstance(value, (bool, int)):
            raise TypeError(
                f"Expected {self.private_name[1:]} to be a bool : received {type(value)} for {value}"
            )
        # try:
        #     bool(value)
        # except Exception as e:
        #     raise ValueError(
        #         f"Impossible to cast {self.private_name[1:]} to bool received {type(value)} for {value} : {e}"
        #     )


class File(Validator):
    """Validator for file paths"""

    def validate(self, value):
        value = value if value else ""
        if not isinstance(value, str):
            raise TypeError(
                f"Expected {self.private_name[1:]} to be a str : received {type(value)} for {value}"
            )

        # if value and (not os.path.isfile(value)):
        #     raise ValueError(
        #         f"Expected {self.private_name[1:]} to be a valid file path : received {value}"
        #     )


class Dir(Validator):
    """Validator for directory paths"""

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f"Expected {self.private_name[1:]} to be a str : received {type(value)} for {value}"
            )

        # if not os.path.isdir(value):
        #     raise ValueError(
        #         f"Expected {self.private_name[1:]} to be a valid directory path : received {value}"
        #     )


class Output(Validator):
    """Validator for output file format"""

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f"Expected {self.private_name[1:]} to be a str : received {type(value)} for {value}"
            )

        # if value not in ["mp3", "mp4"]:
        #     raise ValueError(
        #         f"Expected {self.private_name[1:]} to be a valid file format : received {value}"
        #     )


class Context(Validator):
    """Validator for context"""

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f"Expected {self.private_name[1:]} to be a str : received {type(value)} for {value}"
            )

        value = value.lower()

        # if value not in ["fr", "en"]:
        #     raise ValueError(
        #         f"Expected {self.private_name[1:]} to be a valid context : received {value}"
        #     )


# class Config(Validator):
#     """Validator for config"""

#     DEFAULT_CONFIG = DEFAULT_CONFIG

#     def validate(self, value):
#         if not isinstance(value, dict):
#             raise TypeError(
#                 f"Expected {self.private_name[1:]} to be a dict : received {type(value)} for {value}"
#             )

#         for k, v in self.DEFAULT_CONFIG.items():
#             if k not in value.keys():
#                 logger.warning(f"Missing {k} in config. Using default value {v}")
#                 raise ValueError(
#                     f"Expected {self.private_name[1:]} to be have key {k} : {v}"
#                 )
