from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import insert
from src.database import get_async_session
from src.users.models import User, role


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

async def new_role(session, create_role):
    stmt = insert(role).values(**create_role.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
