# models.py

from sqlalchemy import Column, Integer, String
from db import Base  # Import Base from database.py



class User(Base):
    __tablename__ = 'users'  # Name of the table in PostgreSQL

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
