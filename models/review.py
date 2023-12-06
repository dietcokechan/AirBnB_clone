#!/usr/bin/python3
"""review class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """definition"""
    place_id = ""
    user_id = ""
    text = ""
