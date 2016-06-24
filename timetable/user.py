import bcrypt
from sqlalchemy import Integer, TypeDecorator, Unicode
from sqlalchemy.schema import Column

from .db import Base


__all__ = 'PasswordType', 'Password', 'User',


class PasswordType(TypeDecorator):
    """SQLAlchemy custom type for password cryption. see
    <http://docs.sqlalchemy.org/en/rel_0_9/core/custom_types.html> if you
    want to know about :class:`sqlalchemy.types.TypeDecorator` .
    .. sourcecode:: python
       class ModelHasPassword(Base):
           _password = Column(PasswordType, nullable=False)
    """

    impl = Unicode

    def process_bind_param(self, value, dialect):
        value = Password(value)
        return value.encrypt().decode('utf-8')

    def process_result_value(self, value, dialect):
        return Password(value, encrypted=True)


class Password:
    """Password class for comparison, encryption.
    """

    _encrypted = None

    _plain = None

    def __init__(self, plain, encrypted=False):
        if encrypted:
            self._encrypted = plain
        else:
            self._plain = plain

    def encrypt(self):
        """Encrypt plain text if not encypted.
        :return: encrypted password
        :rtype: str
        """
        if not self._encrypted:
            self._encrypted = bcrypt.hashpw(self._plain.encode('utf-8'),
                                            bcrypt.gensalt())
        return self._encrypted

    def __eq__(self, other):
        """Define equal operator.
        :param a object want to comparision with self.
        :return: ``other`` has same plain text with self.
        :rtype: bool
        """
        password = other
        if isinstance(other, Password):
            password = other._plain
        comparison = bcrypt.hashpw(
            password.encode('utf-8'), self._encrypted.encode('utf-8'))
        return comparison.decode('utf-8') == self._encrypted

    def __ne__(self, other):
        """Define equal operator.
        :param a object want to comparision with self.
        :return: :param other: dosen't have same plain text with self.
        :rtype: bool
        """
        return not (self == other)

    def __str__(self):
        if self._encrypted:
            return self._encrypted
        return self.encrypt()

    def __repr__(self):
        if not self._encrypted:
            self.encrypt()
        return 'Password({})'.format(self._encrypted)


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    password = Column(PasswordType, nullable=False)

    email = Column(Unicode, unique=True, nullable=False)
