from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from di import get_deptest, get_session
from domain import Aircraft, DepTest
from infrastructure import repository

router = APIRouter(prefix="/aircrafts", tags=["aircrafts"])

@router.get(
    '',
    responses={400: {"description": "Bad request"}},
    description="Получение листинга всех типов авиалайнеров",
)
async def get_aircraft(
        class_no : int = 2,
        session: AsyncSession = Depends(get_session)):
    crafts = await repository.get_aircraft(class_no, session)
    return crafts

@router.get(
    '/dptest',
    responses={400: {"description": "Bad request"}},
    #response_model=int,
    description="тест",
)
async def get_aircraft(dptest : DepTest = Depends(get_deptest)):
    return dptest.get_one()


@router.post(
    '',
    responses={400: {"description": "Bad request"}},
    description="Обновление типа авиалайнера",
)
async def update_aircraft(
        code:str = '319',
        velocity:int = 1840,
        session:AsyncSession = Depends(get_session)):
    await repository.update_aircraft(code,velocity,session)

