"""Docstring para backend.app.models.favorite"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Favorite(Base):
    """Docstring para Favorite"""
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    url = Column(String, unique=True, index=True)
    user_id = Column(Integer, index=True)  # Assuming a user_id to associate with a user

    def __repr__(self):
        return f"<Favorite(id={self.id}, title={self.title}, url={self.url}, user_id={self.user_id})>"
