from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, Unicode

from .db import Base


__all__ = 'Category',


class Category(Base):

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)

    name = Column(Unicode, nullable=False)

    parent_id = Column(Integer)

    subjects = relationship('Subject', secondary='subject_category_assoc')
