from sqlalchemy import Engine
from sqlalchemy.ext.asyncio import AsyncEngine


class DepTest:
    engine: AsyncEngine

    def __init__(self, engine: AsyncEngine):
        self.engine = engine

    def get_one(self):
        return 1

    def get_many(self):
        return 1