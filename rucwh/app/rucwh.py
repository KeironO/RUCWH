from flask import Flask, render_template, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import BaseConfig
import os
from db import SkillTable, Account

app = Flask(__name__)

_base_engine_url = "%s:%s@%s/rucwhdb" % (os.environ["postgresql_usr"], os.environ["postgresql_pass"], BaseConfig.POSTGRESQL_ADDR)
engine = create_engine('postgresql+psycopg2://%s' % _base_engine_url, echo=False)

Session = sessionmaker(bind=engine)
session = Session()

@app.route("/")
def rucwh():
    return render_template("index.html", clan_name=BaseConfig.CLAN_NAME)

@app.route("/api",  methods=['POST'])
def api():
    req_data = request.get_json()


    # Will do the calculations server side.

    start_time = req_data["start_time"]
    end_time = req_data["end_time"]
    skill_id = req_data["skill_id"]

    return_dict = {
        "Members" : {},
        "Info" : {
            "Prestige Prize": BaseConfig.PRESTIGE_PRIZE,
            "Prestige Rules" : BaseConfig.PRESTIGE_RULES
        }
    }

    for account in session.query(Account).all():
        info = session.query(SkillTable).filter(SkillTable.account_id == account.id).filter(SkillTable.skill_id == skill_id).filter(SkillTable.timestamp >= start_time).filter(SkillTable.timestamp <= end_time).order_by("timestamp").all()

        if len(info) > 1:
            earliest = info[0]
            latest = info[-1]

            return_dict["Members"][account.username] = {
                "start_xp" : earliest.xp,
                "start_lvl" : earliest.level,
                "end_xp": latest.xp,
                "end_lvl" : latest.level,
                "xp_diff" : latest.xp - earliest.xp,
                "lvl_diff" : latest.level - earliest.level
            }

        elif len(info) == 1:
            only_data = info[0]

            return_dict["Members"][account.username] = {
                "start_xp": only_data.xp,
                "start_lvl": only_data.level,
                "end_xp": only_data.xp,
                "end_lvl": only_data.level,
                "xp_diff": only_data.xp - only_data.xp,
                "lvl_diff": only_data.level - only_data.level
            }


    return jsonify(return_dict)
