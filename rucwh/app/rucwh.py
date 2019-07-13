from flask import Flask, render_template, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import BaseConfig
import os
from db import SkillTable, Account

app = Flask(__name__)

_base_engine_url = "%s:%s@%s/rucwhdb" % (
os.environ["postgresql_usr"], os.environ["postgresql_pass"], BaseConfig.POSTGRESQL_ADDR)
engine = create_engine('postgresql+psycopg2://%s' % _base_engine_url, echo=False)

Session = sessionmaker(bind=engine)
session = Session()


@app.route("/")
def rucwh():
    return render_template("index.html", clan_name=BaseConfig.CLAN_NAME)


@app.route("/api", methods=['POST'])
def api():
    def _response(start, end):
        return {
            "start_xp": start.xp,
            "start_lvl": start.level,
            "end_xp": end.xp,
            "end_lvl": end.level,
            "xp_diff": end.xp - start.xp,
            "lvl_diff": end.level - start.level
        }

    req_data = request.get_json()

    return_dict = {
        "Members": {}
    }

    for account in session.query(Account).all():
        info = session.query(SkillTable).filter(SkillTable.account_id == account.id).filter(
            SkillTable.skill_id == req_data["skill_id"]).filter(SkillTable.timestamp >= req_data["start_time"]).filter(
            SkillTable.timestamp <= req_data["end_time"]).order_by("timestamp").all()

        if len(info) > 1:
            return_dict["Members"][account.username] = _response(info[0], info[-1])

        elif len(info) == 1:
            return_dict["Members"][account.username] = _response(info[0], info[0])

    # Will do the calculations server side.

    return jsonify(return_dict)
