from typing import Any

from pydantic import BaseModel, ConfigDict


class Aircraft(BaseModel):
    #model_config : ConfigDict(from_attributes=True)

    code: str
    model: str
    range: int
    class_no: int
    velocity: int