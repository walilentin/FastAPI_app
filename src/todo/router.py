from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.todo.models import todo
from src.todo.schemas import CreateToDo
from src.todo.utils import all_todo, new_todo, complete_todo, delete_todo_by_id, search_by_id
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import select
router = APIRouter(
    prefix="/todo",
    tags=["ToDo"]
)

templates = Jinja2Templates(directory="templates")
router.mount("/static", StaticFiles(directory="static"), name="static")

@router.post("/create")
async def create_post(add_todo: CreateToDo,session: AsyncSession = Depends(get_async_session)):
    return await new_todo(session,add_todo)


@router.get("/select_by_id")
async def select_by_id(todo_id: int, session: AsyncSession = Depends(get_async_session)):
    return await search_by_id(session, todo_id)


@router.post("/complete_todo")
async def complete_todo(id: int, session: AsyncSession = Depends(get_async_session)):
    return {"message": "Завершено", "items" : await complete_todo(session, id)}


@router.delete("/delete_todo")
async def delete_todo(id: int, session: AsyncSession = Depends(get_async_session)):
    return {"message": "Видалено", "items" : await delete_todo_by_id(session, id)}



