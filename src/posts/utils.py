from sqlalchemy import select, insert

from src.posts.models import Post


async def new_post(session, create_post):
    stmt = insert(Post).values(**create_post.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


async def get_all(session):
    query = select(Post)
    result = await session.scalars(query)
    return result.all()