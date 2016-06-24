from sqlalchemy import Integer, Unicode
from sqlalchemy.schema import Column

from .db import Base


__all__ = 'Subject',


class Subject(Base):

    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)

    name = Column(Unicode, nullable=False)

    category_id = Column(Integer, nullable=False)
