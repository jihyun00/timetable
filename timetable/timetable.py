from .db import Base


class timetable(Base):
    __tablename__ = 'timetables'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, nullable=False)

    semester = Column(, nullable=False)

    subject_id = Column(Integer, nullable=False)
