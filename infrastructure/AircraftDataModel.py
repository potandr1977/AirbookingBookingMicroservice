from sqlalchemy import Column, Integer, Text

from di import Base

class AircraftDataModel(Base):
    __tablename__ = 'aircraft'
    __table_args__ = {'schema': 'postgres_air'}

    code = Column('code',Text, primary_key = True)
    model = Column('model',Text)
    range = Column('range',Integer)
    class_no = Column('class',Integer)
    velocity = Column('velocity',Integer)