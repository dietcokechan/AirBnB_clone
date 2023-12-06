#!/usr/bin/python3
"""user class that inhherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """definition"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
