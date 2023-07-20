from src.users.base_config import fastapi_users, auth_backend
from src.users.schemas import UserRead, UserCreate
from src.operations.router import router as router_operations
from src.pages.router import router as page
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from src.todo.router import router as todo_router
from src.users.router import router as role_router
from fastapi import FastAPI
from tasks.router import router as router_tasks
from fastapi.staticfiles import StaticFiles

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
app.include_router(todo_router)
app.include_router(role_router)
app.include_router(router_tasks)
app.include_router(router_operations)
app.include_router(page)
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)
@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")