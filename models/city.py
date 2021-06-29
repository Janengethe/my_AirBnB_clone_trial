#!/usr/bin/python3
"""
Module city
Has Class City that inherits from BaseModel
"""

from base_model import BaseModel
import json


class City(BaseModel):
    """
    class inherits from BaseModel
    """
    state_id = ""
    name = ""
