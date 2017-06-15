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
    dbsess.execute(
        """
        CREATE KEYSPACE infiniahansom WITH REPLICATION = { 'class' : 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '1' } AND DURABLE_WRITES = true;

CREATE TABLE infiniahansom.hansomdata (
    username text,
    document text,
    PRIMARY KEY (username)
) WITH read_repair_chance = 0.0
   AND dclocal_read_repair_chance = 0.1
   AND gc_grace_seconds = 864000
   AND bloom_filter_fp_chance = 0.01
   AND caching = { 'keys' : 'ALL', 'rows_per_partition' : 'NONE' }
   AND comment = ''
   AND compaction = { 'class' : 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold' : 32, 'min_threshold' : 4 }
   AND compression = { 'chunk_length_in_kb' : 64, 'class' : 'org.apache.cassandra.io.compress.LZ4Compressor' }
   AND default_time_to_live = 0
   AND speculative_retry = '99PERCENTILE'
   AND min_index_interval = 128
   AND max_index_interval = 2048
   AND crc_check_chance = 1.0;

    """
    )
    
