from sqlalchemy import Column, BigInteger, String, sql

from src.utils.db_api.db_gino import TimedBaseModel


class Victim(TimedBaseModel):
    __tablename__ = 'notes'
    id_user = Column(BigInteger)
    id_victim = Column(BigInteger, primary_key=True)
    name = Column(String(255))
    reason = Column(String(255))
    query: sql.Select
