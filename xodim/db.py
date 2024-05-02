from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

engine = create_engine('postgresql+psycopg2://postgres:2005@localhost:5432/postgres', echo=True)


class Base(DeclarativeBase):
    pass


class UserForm(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    surname: Mapped[str] = mapped_column(String(100))
    birth_city: Mapped[str] = mapped_column(String(100))


Base.metadata.create_all(engine)
