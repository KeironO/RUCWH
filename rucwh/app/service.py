import threading
from rssg import RSClan, RSAccount
import datetime
from config import BaseConfig
from joblib import delayed, Parallel
from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData
import os
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SkillTable(Base):
    __tablename__ = "skilltable"

    id = Column(Integer, primary_key=True, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    username = Column(String)
    skill_id = Column(Integer)
    xp = Column(Integer)
    level = Column(Integer)

def _create_engine():
    _base_engine_url = "%s:%s@%s/rucwhdb" % (os.environ["postgresql_usr"], os.environ["postgresql_pass"], BaseConfig.POSTGRESQL_ADDR)
    return create_engine('postgresql+psycopg2://%s' % _base_engine_url, echo=True)

def _get_members_hiscores(name: str):
    hiscores = RSAccount(name).hiscores

def _do_service():
    threading.Timer(BaseConfig.TICKOVER, _do_service).start()
    clan = RSClan(BaseConfig.CLAN_NAME)

    for member in clan.clan_members:
        member = RSAccount(member)
        hiscores = member.hiscores

if __name__ == "__main__":
    engine = _create_engine()
    clan_name = BaseConfig.CLAN_NAME
    clan = RSClan(clan_name)

    if not engine.dialect.has_table(engine, SkillTable):
        Base().metadata.create_all(engine)

    _do_service()
