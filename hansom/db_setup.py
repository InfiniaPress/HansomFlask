from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json
import os

from database.StupidityException import WeirdException

if os.path.isfile("noupload.config.json"):
    with open("noupload.config.json") as cfg:
        conf = json.load(cfg)
else:
    with open("config.json") as cfg:
        conf = json.load(cfg)

dbauth = PlainTextAuthProvider(username=conf['db']['username'], password=conf['db']['password'])
dbcluster = Cluster([conf['db']['hostname']], auth_provider=dbauth)
dbsess = dbcluster.connect(conf['db']['dbname'])

with open("setup.cql") as cql:
    print("You are about to install the Hansom database. Some text will appear. Do not worry")
    print(cql)
    dbsess.execute(cql)
    
