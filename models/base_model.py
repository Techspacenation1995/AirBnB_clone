#!/usr/bin/python3
"""module base_model"""


import uuid
from datetime import datetime
import models


class BaseModel():
    """This is the class BaseModel"""
    def __init__(self, *args, **kwargs):
        """class constructor for class BaseModel"""
        if kwargs:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """The string representation of the BaseModel instance"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Creates an updated version of the 'updated_at'
        instance with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """The dictionary representation of instance"""
        obj_dict = dict(self.__dict__)
        obj_dict['created_at'] = self.__dict__['created_at'].isoformat()
        obj_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return (obj_dict)
