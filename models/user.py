#!/usr/bin/python3
# models/user.py
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base

from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    reviews = relationship("Review", backref="user", cascade="all, delete-orphan")
