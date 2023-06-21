from sqlalchemy import MetaData, Table, Column, Integer, String

from src.database import Base

metadata = MetaData()

post = Table(
    "post",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("body", String, nullable=False),
)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
