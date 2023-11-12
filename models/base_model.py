#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        # Generate a unique identifier for the instance
        self.id = str(uuid.uuid4())
        # Set the creation timestamp to the current date and time
        self.created_at = datetime.now()
        # Set the initial update timestamp to the creation timestamp
        self.updated_at = self.created_at

    def __str__(self):
        # Return a string representation of the object
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        # Update the update timestamp to the current date and time
        self.updated_at = datetime.now()

    def to_dict(self):
        # Create a copy of the instance's attributes dictionary
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
