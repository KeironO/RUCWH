import json
import os



class BaseConfig:
    config_fp = os.path.join(os.path.expanduser("~"), ".rucwh")

    with open(config_fp, "r") as infile:
        _c = json.load(infile)

    CLAN_NAME = _c["clan_name"]
    TICKOVER = _c["tickover"]
    MIN_PART = _c["min_part"]
    PRESTIGE_PRIZE = _c["prestige_part"]
    PRESTIGE_RULES = _c["prestige_rules"]
    POSTGRESQL_ADDR = c["postgresql_addr"] 
