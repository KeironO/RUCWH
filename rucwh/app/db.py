from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData, BigInteger
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class SkillTable(Base):
    __tablename__ = "skilltable"

    id = Column(Integer, primary_key=True, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    username = Column(String)
    skill_id = Column(Integer)
    xp = Column(BigInteger)
    level = Column(Integer)