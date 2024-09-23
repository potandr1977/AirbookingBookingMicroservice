from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from domain.AbstractRepository import AbsractRepository
from domain.Aircraft import Aircraft
from sqlalchemy import Select
from infrastructure.AircraftDataModel import AircraftDataModel, Base

class AircraftRepository(AbsractRepository):
    session: AsyncSession

    def __init__(self,session: AsyncSession):
        self.session = session

    async def get_aircraft(self,class_no: int):
        query = Select(AircraftDataModel).where(AircraftDataModel.class_no == class_no)
        result = await self.session.execute(query)
        models = result.scalars().all()
        if models:
            crafts = []
            for aircraft in models:
                crafts.append(Aircraft(
                    code = aircraft.code,
                    model = aircraft.model,
                    range = aircraft.range,
                    class_no = aircraft.class_no,
                    velocity = aircraft.velocity))
            return crafts

    async def update_aircraft(self,code:str, velocity:int) -> None:
        query = Select(AircraftDataModel).where(AircraftDataModel.code == code)
        result = await self.session.execute(query)
        model = result.scalars().first()
        if model is not None:
            model.velocity = velocity
            await self.session.commit()

'''
data = {
    "code": model.code,
    "model": model.model,
    "range": model.range,
    "classNo": model.classNo,
    "velocity": model.velocity
}
yield Aircraft(**data)
'''
'''
                    aircrafts.append({
                        "code": f"{aircraft.code}",
                        "model": f"{aircraft.model}",
                        "range": f"{aircraft.range}",
                        "class_no": f"{aircraft.class_no}",
                        "velocity": f"{aircraft.velocity}"
                    })
                return JSONResponse(content=aircrafts, status_code=200)
                    '''