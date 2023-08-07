from fastapi import APIRouter, Request, Depends, WebSocket
from fastapi.templating import Jinja2Templates

from src.operations.router import get_specific_operations
from src.todo.router import select_by_id

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router.get("/search/{operation_type}")
def get_search_page(request: Request, operations=Depends(get_specific_operations)):
    return templates.TemplateResponse("search.html", {"request": request, "operations": operations["data"]})


@router.get("/todo/{todo_id}")
def get_todo_page(request: Request, todos=Depends(select_by_id)):
    return templates.TemplateResponse("todo.html", {"request": request, "todos": todos["data"]})

@router.get("/main")
def get_base_page(request: Request):
    return templates.TemplateResponse("main_page.html", {"request": request})

@router.get("/chat")
async def get(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

