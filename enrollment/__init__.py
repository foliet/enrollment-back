import pymysql
from rediscluster import ClusterConnectionPool, RedisCluster
pymysql.install_as_MySQLdb()

nodes = [
    {'host': '10.0.16.17', 'port': 6379},
    {'host': '10.0.4.2', 'port': 6379},
    {'host': '10.0.4.4', 'port': 6379}
]
pool = ClusterConnectionPool(startup_nodes=nodes)
redis_conn = RedisCluster(connection_pool=pool)
