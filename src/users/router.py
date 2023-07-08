from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.users.schemas import RoleCreate
from src.users.utils import new_role

router = APIRouter(
    prefix="/role",
    tags=["Role"]
)


@router.post("")
async def create_role(add_role: RoleCreate,session: AsyncSession = Depends(get_async_session)):
    return await new_role(session,add_role)


