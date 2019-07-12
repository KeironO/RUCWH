from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
from config import BaseConfig
import os
from db import SkillTable

app = Flask(__name__)

_base_engine_url = "%s:%s@%s/rucwhdb" % (os.environ["postgresql_usr"], os.environ["postgresql_pass"], BaseConfig.POSTGRESQL_ADDR)
engine = create_engine('postgresql+psycopg2://%s' % _base_engine_url, echo=True)

@app.route("/")
def rucwh():
    return render_template("index.html")

@app.route("/api/test/<skill_id>")
def test(skill_id):

    return jsonify({"entry" : skill_id})
