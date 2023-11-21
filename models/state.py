# models/state.py
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """Initialization of the state instance"""
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        dictionary = super().to_dict()
        if 'cities' in dictionary:
            del dictionary['cities']
        return dictionary
