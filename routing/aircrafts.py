from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from di import get_deptest, get_session
from domain import Aircraft, DepTest, service
from infrastructure import AircraftRepository
from infrastructure.AircraftRepository import AircraftRepository

router = APIRouter(prefix="/aircrafts", tags=["aircrafts"])

@router.get(
    '',
    responses={400: {"description": "Bad request"}},
    description="Получение листинга всех типов авиалайнеров",
)
async def get_aircraft(
        class_no : int = 2,
        session: AsyncSession = Depends(get_session)):
    repository = AircraftRepository(session)
    crafts = await service.get_aircraft(class_no,repository)
    return crafts

@router.post(
    '',
    responses={400: {"description": "Bad request"}},
    description="Обновление типа авиалайнера",
)
async def update_aircraft(
        code:str = '319',
        velocity:int = 1840,
        session:AsyncSession = Depends(get_session)):
    repository = AircraftRepository(session)
    await repository.update_aircraft(code,velocity)

@router.get(
    '/dptest',
    responses={400: {"description": "Bad request"}},
    #response_model=int,
    description="тест",
)
async def get_aircraft(dptest : DepTest = Depends(get_deptest)):
    return dptest.get_one()