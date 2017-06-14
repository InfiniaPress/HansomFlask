from cassandra.cluster import Cluster
import json
from StupidityException import WeirdException


with open("../../../config.json") as cfg:
    conf = json.load(cfg)


dbcluster = Cluster([conf['db']['hostname']])
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
    (name)
    
  )
  return stmt['document']
def checkNoteExists(name):
  stmt = dbsess.execute("SELECT * FROM hansomdata WHERE username = %s")
  if len(stmt) != 0:
    return False
  elif len(stmt) == 0:
    return True
  else:
    raise WeirdException("Cassandra didn't return a proper row. Wat")