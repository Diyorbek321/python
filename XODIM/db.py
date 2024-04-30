from typing import Optional
from sqlalchemy import String, Integer, create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

engine = create_engine('postgresql+psycopg2://postgres:Diyorbek2005@localhost/telegram')


class Base(DeclarativeBase):
    pass


class UserForm(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    surname: Mapped[str] = mapped_column(String(30))
    birthday: Mapped[int] = mapped_column(Integer)
    photo: Mapped[str] = mapped_column(String(255))


Base.metadata.create_all(engine)
