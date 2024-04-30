from datetime import datetime

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
import os

Base_Dir = os.path.dirname(os.path.realpath(__file__))

connection_string = 'sqlite:///'+os.path.join(Base_Dir, 'site.db')

base = declarative_base()

engine = create_engine(connection_string,echo=True)
"""
class User
    id int
    name str
    email str
    date_created datetime
"""


class User(base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(80), unique=True, nullable=False)
    date_creates = Column(DateTime(), default=datetime)

    def __repr__(self):
        return f'<User username={self.username}, email = {self.email}>'


new_user = User(id=11, username="Diyorbek", email="asdasdas@gmail.com")
print(new_user)
