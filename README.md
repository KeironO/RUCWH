# RUCWH
RUnescape Clan Week Helper


## Installation and Setup

### Postgresql Setup

If you're using a Debian-based OS, then install postgresql using apt:

```
sudo apt install postgresql
```

After installing PostgreSQL database server, by default it creates a user ‘postgres’ with role ‘postgres’. It also creates a system account with same name ‘postgres’. So to connect to postgres server, login to your system as user postgres and connect database.

```
sudo -i -u postgres
```

Now to create a user for RUCWH, I'd recommend using the ```createuser``` command.

```
createuser --interactive
```

Once you've set up a new psql user, you now need to create the database using the following commands.

```
createdb rucwhdb
psql -d rucwhdb
```

And now you need to attach a password to your user account, using the following command.

```
ALTER USER uid WITH PASSWORD 'password';
```

Ensuring to replace ```uid``` and ```password``` to your credentials.


## Configuration File

Create a file in your home directory called .rucwh, and put the following in it:

```
{
    "clan_name": "", # Name of clan inside the quotation
    "tickover" : 60, # Amount of time the RS API is indexed
    "min_part" : 1.0, # Minmum % of overall clan xp required to participate
    "prestige_prize: : 8.5, # % of total GP that's kept for the prestiege prize
    "prestige_rules" : [60, 30, 10] # % of prestige prize for 1-3 
    "postgresql_addr": ""
}
```
