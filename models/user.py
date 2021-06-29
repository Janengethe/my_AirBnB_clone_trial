#!/usr/bin/python3
"""
Module user
Inherits from BaseModel
With class attributes email, password, first_name, last_name
"""

from models.base_model import BaseModel
import json

class User(BaseModel):
    """
    Class User inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
