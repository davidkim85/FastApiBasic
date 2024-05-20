from typing import Annotated
from fastapi import Depends, status, Query, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from api.database import get_async_session
from api.models.models import Post
from api.schemas.PostSchema import PostRead, PostCreate

router = APIRouter()


@router.post("/posts", response_model=PostRead, status_code=status.HTTP_201_CREATED)
async def create_post(Title: Annotated[str, Query(description="Please Insert Title Value:")],
                      Content: Annotated[str, Query(description="Please Insert Value:")], post_create: PostCreate,
                      session: AsyncSession = Depends(get_async_session)) -> Post:
    post_create.content = Content
    post_create.title = Title
    post = Post(**post_create.dict())
    session.add(post)
    await session.commit()
    return post
