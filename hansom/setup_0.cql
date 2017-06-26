CREATE KEYSPACE IF NOT EXISTS infiniahansom WITH REPLICATION = { 'class' : 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '1' } AND DURABLE_WRITES = true;
