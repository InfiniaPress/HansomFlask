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


with open("setup.cql", "r") as setup_cql:
    print("Loading CQL")
    stp_cql = setup_cql.read().replace("\n", "")
    print("CQL: " + stp_cql)
    dbsess.execute(stp_cql)
    setup_cql.close()