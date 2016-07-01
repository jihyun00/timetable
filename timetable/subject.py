from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, Unicode

from .db import Base


__all__ = 'SubjectCategoryAssoc', 'Subject',


class SubjectCategoryAssoc(Base):

    __tablename__ = 'subject_category_assoc'

    subject_id = Column(Integer, ForeignKey('subjects.id'))

    category_id = Column(Integer, ForeignKey('categories.id'))

    subject = relationship('Subject')

    category = relationship('Category')


class Subject(Base):

    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)

    name = Column(Unicode, nullable=False)

    timetables = relationship('Timetable', secondary='timetable_subject_assoc')
