import redis

# Connect to ElastiCache Redis
client = redis.StrictRedis(host='rediscluster.eulx8y.ng.0001.use1.cache.amazonaws.com', port=6379, db=0)

# Publish a message  
def publish_message(channel, message):
    client.publish(channel, message)
    print(f"Published message: {message} to channel: {channel}")

publish_message("my_channel","Hello")

