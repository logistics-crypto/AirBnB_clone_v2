#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.state import State
from models import storage

class City(BaseModel, Base):
    """ City Module for HBNB project """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship('Place', backref='city', cascade='all, delete')

    def __init__(self, *args, **kwargs):
        """Initialization of the city instance"""
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        dictionary = super().to_dict()
        if 'state' in dictionary:
            del dictionary['state']
        return dictionary

    if storage_type != "db":
        @property
        def state(self):
            """Getter method for the state attribute"""
            from models import storage
            state = storage.get(State, self.state_id)
            return state
