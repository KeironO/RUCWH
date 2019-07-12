import threading
from sqlalchemy.orm import sessionmaker
from rssg import RSClan, RSAccount
import datetime
from config import BaseConfig
from joblib import delayed, Parallel
from sqlalchemy import create_engine
import os
from db import SkillTable, Base


def _create_engine():
    _base_engine_url = "%s:%s@%s/rucwhdb" % (os.environ["postgresql_usr"], os.environ["postgresql_pass"], BaseConfig.POSTGRESQL_ADDR)
    return create_engine('postgresql+psycopg2://%s' % _base_engine_url, echo=True)

def _get_members_hiscores(name: str, engine):
    hiscores = RSAccount(name).hiscores

def _do_service(session):
    threading.Timer(BaseConfig.TICKOVER, _do_service, [session]).start()
    clan = RSClan(BaseConfig.CLAN_NAME)

    for member in clan.clan_members:
        member = RSAccount(member)
        hiscores = member.hiscores
        if hiscores != None:
            most_rec = session.query(SkillTable).filter(SkillTable.username == member.username).filter(SkillTable.skill_id == 0).order_by("timestamp").first().xp
            if hiscores["Overall"]["XP"] > most_rec:
                for scount, sid  in enumerate(hiscores.keys()):
                    st = SkillTable()
                    st.username = member.username
                    st.skill_id = scount
                    st.xp = int(hiscores[sid]["XP"])
                    st.level = hiscores[sid]["Level"]
                    session.add(st)
                    session.commit()

def test(session):
    #print(session.query(SkillTable).filter(SkillTable.username == "Svephen").filter(SkillTable.skill_id == 0).order_by("timestamp").first().xp)
    pass

if __name__ == "__main__":
    engine = _create_engine()
    clan_name = BaseConfig.CLAN_NAME
    clan = RSClan(clan_name)

    if not engine.dialect.has_table(engine, SkillTable):
        Base().metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    _do_service(session)
    #test(session)
