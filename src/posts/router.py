from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.posts.schemas import CreatePost
from src.posts.utils import new_post, get_all

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get("")
async def get_posts(session: AsyncSession = Depends(get_async_session)):
    return await get_all(session)


@router.post("")
async def create_post(add_post: CreatePost,session: AsyncSession = Depends(get_async_session)):
    return await new_post(session,add_post)


