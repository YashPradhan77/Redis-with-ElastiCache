import redis

redis_client = redis.StrictRedis(
    host='PRIMARY-ENDPOINT', 
    port=6379, 
    decode_responses=True
)

def cache_set(key, value, expire_seconds=None):
    redis_client.set(name=key, value=value, ex=expire_seconds)
    print(f"Cached: {key} = {value}")

def cache_get(key):
    value = redis_client.get(name=key)
    print(f"Retrieved from cache: {key} = {value}")
    return value

cache_set('key', 'value', expire_seconds=3600)
cache_get('key')
