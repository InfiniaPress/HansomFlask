import json


with open("../../../config.json") as cfg:
    conf = json.load(cfg)

PyMongoDB_URI = "mongodb://{username}:{password}@{hostname}/{databasename}".format(
    username=conf['db']['username'],
    password=conf['db']['password'],
    hostname=conf['db']['hostname'],
    databasename=conf['db']['dbname'],
)

