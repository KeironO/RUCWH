# RUCWH
RUnescape Clan Week Helper written on my week off.


## Installation and Setup

### Postgresql Setup

If you're using a Debian-based OS, then install postgresql using apt:

```bash
sudo apt install postgresql  postgresql-server-dev-all python3-dev
```

After installing PostgreSQL database server, by default it creates a user ‘postgres’ with role ‘postgres’. It also creates a system account with same name ‘postgres’. So to connect to postgres server, login to your system as user postgres and connect database.

```bash
sudo -i -u postgres
```

Now to create a user for RUCWH, I'd recommend using the ```createuser``` command.

```bash
createuser --interactive
```

Once you've set up a new psql user, you now need to create the database using the following commands.

```postgresql
createdb rucwhdb
psql -d rucwhdb
```

And now you need to attach a password to your user account, using the following command.

```postgresql
ALTER USER uid WITH PASSWORD 'password';
```

Ensuring to replace ```uid``` and ```password``` to your credentials.


### Configuration File

Create a file in your home directory called .rucwh, and put the following in it:

```json
{
    "clan_name": "", # Name of clan inside the quotation
    "tickover" : 60, # Amount of time the RS API is indexed
    "min_part" : 1.0, # Minmum % of overall clan xp required to participate
    "prestige_prize: : 8.5, # % of total GP that's kept for the prestiege prize
    "prestige_rules" : [60, 30, 10] # % of prestige prize for 1-3 
    "postgresql_addr": ""
}
```

### Systemd Service

The thing that "gets" the account information acts as a systemd service (meaning that it runs in the background, and once setup requires no further interference from you).



## Environment Variables

Due to the relative inimportance of the data held within the database, I've opted to just store them as environment variables.

In your terminal, type the following:

```
export postgresql_usr=keo7
export postgresql_pass=local
```

Changing the username and password where necessary.

# API Documentation

The API itself is incredibly simplistic, all you do is post something like...
```json
{
	"start_time" : "2019-07-12T23:43:44.642Z",
	"end_time" : "2019-07-13T23:43:44.642Z",
	"skill_id" : 0
}
```

to ```/api``` and it returns a JSON response wherein each user is a key.

```json
{
    "08009292": {
        "end_lvl": 1952,
        "end_xp": 80812959,
        "lvl_diff": 0,
        "start_lvl": 1952,
        "start_xp": 80812959,
        "xp_diff": 0
    },
    "4grace1": {
        "end_lvl": 2396,
        "end_xp": 206198264,
        "lvl_diff": 0,
        "start_lvl": 2396,
        "start_xp": 206198264,
        "xp_diff": 0
    },
    "Abaddont": {
        "end_lvl": 2377,
        "end_xp": 188616092,
        "lvl_diff": 0,
        "start_lvl": 2377,
        "start_xp": 188616092,
        "xp_diff": 0
    },
    ...
   }
```
