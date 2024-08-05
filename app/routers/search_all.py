from fastapi import APIRouter, Depends, status, Query
from app.database.database import get_db
from app.database.cruds.search import search_by_title;
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.schemas import payload
from datetime import date



search_router = APIRouter()

@search_router.get("/search")
async def search_by_query(title: str= Query(description="Exercise or Lesson title"), db: AsyncSession=Depends(get_db)):
    return payload.BaseResponse(
        date=date.today(),
        status=status.HTTP_200_OK,
        payload=await search_by_title(title, db),
        message="Search results"
    )
