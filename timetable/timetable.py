from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Date, Integer

from .db import Base


__all__ = 'TimetableSubjectAssoc', 'Timetable',


class TimetableSubjectAssoc(Base):

    __tablename__ = 'timetable_subject_assoc'

    timetable_id = Column(Integer, ForeignKey('timetables.id'))

    subject_id = Column(Integer, ForeignKey('subjects.id'))

    timetable = relationship('Timetable')

    subject = relationship('Subject')


class Timetable(Base):

    __tablename__ = 'timetables'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))

    semester = Column(Date, nullable=False)

    user = relationship('User')

    subjects = relationship('Subject', secondary='timetable_subject_assoc')
