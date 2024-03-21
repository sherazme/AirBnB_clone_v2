#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import models
from os import getenv
from models.base_model import Base
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get list of related Cities"""
            c_l = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    c_l.append(city)
            return c_l
