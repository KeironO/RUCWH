import pandas as pd
import urllib3
import json
from io import StringIO

pm = urllib3.PoolManager()

class RSAccount:
    def __init__(self, username: str):
        self.username = username

    @property
    def profile(self):
        _acc_url = "https://apps.runescape.com/runemetrics/profile/profile?user=%s" % (self.username)

        _r = pm.request("GET", _acc_url)
        if _r.status == 200:
            return json.loads(_r.data.decode("utf-8"))

    @property
    def logged_in(self) -> bool:
        return self.profile["loggedIn"] == "true"

    @property
    def combatlvl(self) -> int:
        return int(self.profile["combatlevel"])

    @property
    def hiscores(self) -> dict:
        _stats_url = "https://secure.runescape.com/m=hiscore/index_lite.ws?player=%s" % (self.username)
        _r = pm.request("GET", _stats_url)

        if _r.status == 200:
            df = pd.read_csv(StringIO(_r.data.decode("utf-8")), header=None)
            df.columns = ["Rank", "Level", "XP"]
            df = df.iloc[0:24]

            df.index = [
                "Overall",
                "Attack",
                "Defence",
                "Strength",
                "Hitpoints",
                "Ranged",
                "Prayer",
                "Magic",
                "Cooking",
                "Woodcutting",
                "Fletching",
                "Fishing",
                "Firemaking",
                "Crafting",
                "Smithing",
                "Mining",
                "Herblore",
                "Agility",
                "Thieving",
                "Slayer",
                "Farming",
                "Runecrafting",
                "Hunter",
                "Construction"
            ]

            return df.T.to_dict()
