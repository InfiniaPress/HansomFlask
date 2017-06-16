from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json
import os

from database.StupidityException import WeirdException

if os.path.isfile("../noupload.config.json"):
    with open("../noupload.config.json") as cfg:
        conf = json.load(cfg)
else:
    with open("../config.json") as cfg:
        conf = json.load(cfg)

dbauth = PlainTextAuthProvider(username=conf['db']['username'], password=conf['db']['password'])
dbcluster = Cluster([conf['db']['hostname']], auth_provider=dbauth)
dbsess = dbcluster.connect(conf['db']['dbname'])



class DBNote():
    def __init__(self, name, contents, cassandrasess):
        self.name = name
        self.contents = contents
        self.dbsess = cassandrasess


    def updateDB(self):
        stmt = dbsess.prepare(
            """
            UPDATE hansomdata SET document = ? WHERE username = ?
            """
        )
        dbsess.execute(stmt, (self.contents, self.name))

        return True


def getNote(name):
    stmt = dbsess.prepare("SELECT * FROM hansomdata WHERE username = ?")
    rtn = dbsess.execute(stmt, (name, ))
    for row in rtn:
        return row[1]
    #return stmt.current_rows['document']
def checkNoteExists(name):
    stmt = dbsess.prepare("SELECT * FROM hansomdata WHERE username = ?")
    rtn = dbsess.execute(stmt, (name, ))
    if len(rtn.current_rows) != 0:
        return True
    elif len(rtn.current_rows) == 0:
        return False
    else:
        raise WeirdException("Cassandra didn't return a proper row. Wat")