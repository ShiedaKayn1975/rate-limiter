import redis
import os

def redis_connection():
    redis_host = os.getenv('REDIS_HOST', 'localhost')
    redis_port = os.getenv('REDIS_PORT', 6379)
    connection = redis.Redis(host=redis_host, port=redis_port, socket_connect_timeout=1)

    return connection