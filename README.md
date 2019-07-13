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
    "clan_name": "",
    "tickover" : 60, 
    "min_part" : 1.0, 
    "prestige_prize" : 8.5,
    "prestige_rules" : [60, 30, 10], 
    "postgresql_addr": ""
}
```

### Systemd Service

The thing that "gets" the account information acts as a systemd service (meaning that it runs in the background, and once setup requires no further interference from you).

As I'm quite lazy, I don't want to give you a service file to do this - but I will be nice enough to give you an example one below.

```
[Unit]
Description=service to get RS information
After=network.target

[Service]
Environment=postgresql_usr=keo7
Environment=postgresql_pass=local
User=keo7
Group=www-data
WorkingDirectory=/path/to/RUCWH/rucwh/app
Environment="PATH=/path/to/RUCWH/env/bin"
ExecStart=/path/to/RUCWH/env/bin/python service.py

[Install]
WantedBy=multi-user.target

```

Change whatever you need to make it work, and throw it into ```/etc/systemd/system/``` as ```rucwhs.service```.

Now enable it:

```
sudo systemctl enable rucwhs
```

And start it:

```
sudo systemctl start rucwhs
```

Check if it works, I get the following:

```
  ~ sudo systemctl status rucwhs.service
● rucwhs.service - service to get RS information
   Loaded: loaded (/etc/systemd/system/rucwhs.service; enabled; vendor preset: enabled)
   Active: active (running) since Sat 2019-07-13 02:40:07 BST; 2s ago
 Main PID: 16479 (python)
    Tasks: 2 (limit: 4915)
   CGroup: /system.slice/rucwhs.service
           └─16479 /home/keo7/Projects/RUCWH/env/bin/python service.py

```

Now, don't touch it.

## Environment Variables

Due to the relative inimportance of the data held within the database, I've opted to just store them as environment variables.

In your terminal, type the following:

```
export postgresql_usr=keo7
export postgresql_pass=local
```

Changing the username and password where necessary.

## Yarn

```
yarn install --modules-folder ./app/static/node_modules
```

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


