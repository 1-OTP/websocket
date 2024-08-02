from fastapi import APIRouter, HTTPException, Depends, status
from app.database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.cruds.vocabulary import create_vocabulary, get_all_vocabularies, find_vocabulary_by_level, delete_vocabulary,get_vocabulary_byuuid
from app.database.schemas.vocabulary import CreateVocabularyDto
from app.database.schemas import payload
from datetime import date

vocabulary_router = APIRouter()

@vocabulary_router.post("/vocabularies/")
async def add_new_grammar(vocab:CreateVocabularyDto, db:AsyncSession=Depends(get_db)):
    return payload.BaseResponse(
        date=date.today(),
        status=status.HTTP_201_CREATED,
        payload=await create_vocabulary(vocab, db),
        message="Vocabulary has been created successfully 😉😎"
    )

@vocabulary_router.get("/vocabularies/")
async def list_all_grammars(db:AsyncSession=Depends(get_db)):
    return payload.BaseResponse(
        date=date.today(),
        status=status.HTTP_200_OK,
        payload=await get_all_vocabularies(db),
        message="List of all vocabularyies"
    )

@vocabulary_router.get("/vocabularies/{level}")
async def get_one_grammar(level:str, db:AsyncSession=Depends(get_db)):
    return payload.BaseResponse(
        date=date.today(),
        status=status.HTTP_200_OK,
        payload=await find_vocabulary_by_level(level, db),
        message="Found of all vocabularyies"
    )

@vocabulary_router.delete("/vocabularies/delete")
async def delete_vocab_by_uuid(uuid:str, db:AsyncSession=Depends(get_db)):
    return payload.BaseResponse(
        date=date.today(),
        status=status.HTTP_200_OK,
        payload= await delete_vocabulary(uuid,db),
        message="Vocabulary has been deleted successfully"
    )

@vocabulary_router.get("/vocabularies/vocab-detail/")
async def get_vocabulary_by_uuid(uuid:str, db:AsyncSession=Depends(get_db)):
    return payload.BaseResponse(
        date=date.today(),
        status=status.HTTP_200_OK,
        payload=await get_vocabulary_byuuid(uuid, db),
        message="Vocabulary details"
    )