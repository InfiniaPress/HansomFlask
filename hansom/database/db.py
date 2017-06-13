from cassandra.cluster import Cluster
import json


with open("../../../config.json") as cfg:
    conf = json.load(cfg)

PyMongoDB_URI = "mongodb://{username}:{password}@{hostname}/{databasename}".format(
    username=conf['db']['username'],
    password=conf['db']['password'],
    hostname=conf['db']['hostname'],
    databasename=conf['db']['dbname'],
)


dbcluster = Cluster([conf['db']['hostname']])
dbsess = dbcluster.connect(conf['db']['dbname'])


class Note():
  def __init__
