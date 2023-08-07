from fastapi import HTTPException
from sqlalchemy import select, insert, delete, update
from src.todo.models import ToDo, todo


async def new_todo(session, create_todo):
    stmt = insert(ToDo).values(**create_todo.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


async def search_by_id(session, todo_id):
    query = select(todo).where(todo.c.id == todo_id)
    result = await session.execute(query)
    return {"data": result.all()}



async def all_todo(session):
    query = select(ToDo)
    result = await session.scalars(query)
    return result.all()


async def complete_todo(session, todo_id):
    stmt = update(ToDo).where(ToDo.id == todo_id).values(is_completed=True)
    result = await session.execute(stmt)
    affected_rows = result.rowcount
    if affected_rows == 0:
        raise HTTPException(status_code=404, detail="Завдання не знайдено")
    await session.commit()


async def delete_todo_by_id(session, todo_id):
    stmt = delete(ToDo).where(ToDo.id == todo_id)
    result = await session.execute(stmt)
    affected_rows = result.rowcount
    if affected_rows == 0:
        raise HTTPException(status_code=404, detail="Завдання не знайдено")
    await session.commit()
