from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.todo.schemas import CreateToDo
from src.todo.utils import get_all, new_todo, get_todo_by_id, complete_todo, delete_todo_by_id
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

router = APIRouter(
    prefix="/todo",
    tags=["ToDo"]
)

templates = Jinja2Templates(directory="templates")
router.mount("/static", StaticFiles(directory="static"), name="static")

@router.post("/items")
async def create_post(add_todo: CreateToDo,session: AsyncSession = Depends(get_async_session)):
    return await new_todo(session,add_todo)

@router.get("", response_class=HTMLResponse)
async def items(request: Request,session: AsyncSession = Depends(get_async_session)):
    return templates.TemplateResponse("item.html", {"request": request, "items": await get_all(session)})

@router.get("/items/{id}", response_class=HTMLResponse)
async def items(request: Request, id: int, session: AsyncSession = Depends(get_async_session)):
    return templates.TemplateResponse("item.html", {"request": request, "items": [await get_todo_by_id(session, id)]})


@router.post("/items/{id}/complete")
async def complete_item(id: int, session: AsyncSession = Depends(get_async_session)):
    return {"message": "Завершено", "items" : await complete_todo(session, id)}


@router.delete("/items/{id}")
async def delete_item(id: int, session: AsyncSession = Depends(get_async_session)):
    return {"message": "Видалено", "items" : await delete_todo_by_id(session, id)}