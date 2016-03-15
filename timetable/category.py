from sqlalchemy import Integer, Unicode
from sqlalchemy.schema import Column


from .db import Base


__all__ = 'Category',


class Category(Base):
    
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)

    name = Column(Unicode, nullable=False)

    parent_id = Column(Integer, nullable=False)
