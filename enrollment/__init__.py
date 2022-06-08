import pymysql
import redis

pymysql.install_as_MySQLdb()

pool = redis.ConnectionPool(host='10.0.16.17', port=6379, password='fqh66545896.')
redis_conn = redis.Redis(connection_pool=pool)
