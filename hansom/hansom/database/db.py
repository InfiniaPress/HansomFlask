import json
from sqlalchemy import create_engine

with open("config.json") as cfg:
    json = json.loads(cfg)

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username=cfg['db']['username'],
    password=cfg['db']['password'],
    hostname=cfg['db']['hostname'],
    databasename=cfg['db']['dbname'],
)

db = create_engine(SQLALCHEMY_DATABASE_URI, pool_recycle=299)