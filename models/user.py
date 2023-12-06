#!/usr/bin/python3
"""user class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """definition"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
