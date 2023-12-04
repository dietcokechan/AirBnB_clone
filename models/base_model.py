#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime


class BaseModel:
    """definition"""
    def __init__(self):
        """initialize class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """string representation"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
    
    def __repr__(self):
        """returns string"""
        return self.__str__()
    
    def save(self):
        """save class"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """return dict of object"""
        dic = dict(self.__dict__)
        dic['__class__'] = str(self.__class__.__name__)
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic