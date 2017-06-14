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



class DBNote():
    def __init__(self, name, contents, cassandrasess):
        self.name = name
        self.contents = contents
        self.dbsess = cassandrasess


    def updateDB(self):
        stmt = dbsess.execute(
            """
            BATCH BEGIN;
            UPDATE hansomdata
            SET document = %s
            WHERE username = %s IF EXISTS
            INSERT INTO hansomdata (username, document)
            VALUES (%s, %s) IF NOT EXISTS
            BATCH END;
            """,
            (self.name, self.contents)
        )
        return True


def getNote(name):
    stmt = dbsess.execute(
        """
        SELECT * FROM hansomdata
        WHERE username = %s
        """,
        (name, )

    )
    for row in stmt:
        return row.document
    #return stmt.current_rows['document']
def checkNoteExists(name):
    stmt = dbsess.execute("SELECT * FROM hansomdata WHERE username = %s", (name, ))
    if len(stmt.current_rows) != 0:
        return True
    elif len(stmt.current_rows) == 0:
        return False
    else:
        raise WeirdException("Cassandra didn't return a proper row. Wat")