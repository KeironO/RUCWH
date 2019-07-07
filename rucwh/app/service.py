from rssg import RSClan, RSAccount
from config import BaseConfig
from joblib import delayed, Parallel


if __name__ == "__main__":
    clan_name = BaseConfig.CLAN_NAME
    clan = RSClan(clan_name)
