from sqlalchemy import Integer
from sqlalchemy.schema import Column, ForeignKey

from .db import Base


__all__ = '',


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    password = Column(PasswordType, nullable=False)

    email = Column(, nullable=False, )
