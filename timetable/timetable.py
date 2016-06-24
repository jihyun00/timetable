from sqlalchemy import Date, Integer
from sqlalchemy.schema import Column

from .db import Base


__all__ = 'Timetable',


class Timetable(Base):

    __tablename__ = 'timetables'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, nullable=False)

    semester = Column(Date, nullable=False)

    subject_id = Column(Integer, nullable=False)
