from sqlalchemy import create_engine, Column, Integer, String, DateTime, BigInteger, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, unique=True)


class SkillTable(Base):
    __tablename__ = "skilltable"

    id = Column(Integer, primary_key=True, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    skill_id = Column(Integer)
    xp = Column(BigInteger)
    level = Column(Integer)
    account_id = Column(Integer, ForeignKey("account.id"))
