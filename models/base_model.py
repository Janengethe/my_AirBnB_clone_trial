#!/usr/bin/python3
"""

"""


import models
import uuid
from datetime import datetime
class BaseModel:

  def __init__(self, *args, **kwargs):
    """
    {'updated_at': '2021-06-24T08:39:05.415451', 'id': '64b49857-25d1-49f0-8a58-e67c60ff53b0', 'created_at': '2021-06-24T08:39:05.415432', '__class__': 'BaseModel'}
    """
    if kwargs:
      for k, v in kwargs.items():
        if kwargs[k] == "id":
          self.id = v
        elif kwargs[k] == "created_at":
          self.created_at = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
        elif kwargs[k] == "updated_at":
          self.updated_at = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
        else:
          pass
    else:
      self.id = str(uuid.uuid4())
      self.created_at = datetime.now()
      self.updated_at = datetime.now()

  def __str__(self):
    return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

  def __repr__(self):
    return (self.__str__())

  def save(self):
    models.storage.new(self.to_dict())
    models.storage.save()
    self.updated_at = datetime.now()

  def to_dict(self):
    my_dict = self.__dict__
    my_dict["__class__"] = self.__class__.__name__
    for k, v in my_dict.items():
      if k == "created_at" or k == "updated_at":
        my_dict[k] = v.isoformat()
      else:
        my_dict[k] = v
    return my_dict
