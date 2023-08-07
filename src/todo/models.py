
from sqlalchemy import Table, MetaData, Column, Integer, String, Boolean, ForeignKey

from src.database import Base
from src.users.models import user

metadata = MetaData()


todo = Table(
    "todo",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("author_id", Integer, ForeignKey(user.c.id)),
    Column("is_completed", Boolean, default=False),
)



class ToDo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey(user.c.id))
    is_completed = Column(Boolean, default=False)