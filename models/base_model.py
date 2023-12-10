#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """definition"""
    def __init__(self, *args, **kwargs):
        """initialize class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '`%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

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
        models.storage.save()

    def to_dict(self):
        """return dict of object"""
        dic = dict(self.__dict__)
        dic['__class__'] = str(self.__class__.__name__)
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
