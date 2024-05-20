from typing import Annotated
from fastapi import APIRouter, status, Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.database import get_async_session
from api.models.models import User
from api.schemas.UserSchema import UserCreate,UserRead

router = APIRouter()


@router.post("/users", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_post(Email: Annotated[str, Query(description="Please Insert Title Value:")],user_create: UserCreate,
                      session: AsyncSession = Depends(get_async_session)) -> User:
    user_create.email=Email
    user = User(**user_create.dict())
    session.add(user)
    await session.commit()
    return user
