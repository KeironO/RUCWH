import urllib3
from io import StringIO
import pandas as pd

pm = urllib3.PoolManager()

class RSClan:
    def __init__(self, name: str):
        self.name = name
        self._clan_list = self._get_clan_list()

    def _get_clan_list(self) -> dict:
        _clan_url = "http://services.runescape.com/m=clan-hiscores/members_lite.ws?clanName=%s" % (self.name)

        _r = pm.request("GET", _clan_url)
        if _r.status == 200:
            df = pd.read_csv(StringIO(_r.data.decode("ISO-8859-1")), index_col=0)
            return df.T.to_dict()

    @property
    def clan_members(self):
        return list(self._clan_list.keys())
