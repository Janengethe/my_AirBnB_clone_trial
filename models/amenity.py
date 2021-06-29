#!/usr/bin/python3
"""
Module amenity
Has class Amenity that inherits from BaseModel
"""

from models.base_model import BaseModel
import json

class Amenity(BaseModel):
    """
    Inherits from BaseModel
    Public class attribute name: (str)
    """
    name = ""
