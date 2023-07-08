from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Table, MetaData, Column, Integer, String, JSON, Boolean, ForeignKey, TIMESTAMP

from src.database import Base

metadata = MetaData()


todo = Table(
    "todo",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("is_completed", Boolean, default=False),
)



class ToDo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    is_completed = Column(Boolean, default=False)