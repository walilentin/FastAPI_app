from src.users.base_config import fastapi_users, auth_backend
from src.users.schemas import UserRead, UserCreate
from src.posts.router import router as post_router
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.todo.router import router as todo_router
from src.users.router import router as role_router


app = FastAPI(title="APP")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(post_router)
app.include_router(todo_router)
app.include_router(role_router)


