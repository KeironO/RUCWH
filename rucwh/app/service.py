from rssg import RSClan, RSAccount
import datetime
from config import BaseConfig
from joblib import delayed, Parallel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
import os
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SkillTable(Base):
    __tablename__ = "skilltable"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    username = Column(String)
    skill_id = Column(Integer)
    xp = Column(Integer)
    level = Column(Integer)

def _create_engine():
    _base_engine_url = "%s:%s@%s/rucwhdb" % (os.environ["postgresql_usr"], os.environ["postgresql_pass"], BaseConfig.POSTGRESQL_ADDR)
    return create_engine('postgresql+psycopg2://%s' % _base_engine_url)

if __name__ == "__main__":
    engine = _create_engine()
    clan_name = BaseConfig.CLAN_NAME
    clan = RSClan(clan_name)
