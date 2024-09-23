from typing import List

from domain import AbstractRepository
from domain.Aircraft import Aircraft


async def get_aircraft(class_no: int, repository:AbstractRepository) -> List[Aircraft]:
    return await repository.get_aircraft(class_no)

async def update_aircraft(code:str, velocity:int, repository:AbstractRepository) -> None:
    await repository.update_aircraft(code,velocity)


