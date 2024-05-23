import redis

# Connect to ElastiCache Redis
client = redis.StrictRedis(host='rediscluster.eulx8y.ng.0001.use1.cache.amazonaws.com', port=6379, db=0)

# Publish a message
# client.publish('my_channel', 'Hello, Redis Pub/Sub!')
    
def publish_message(channel, message):
    client.publish(channel, message)
    print(f"Published message: {message} to channel: {channel}")

if __name__ == "__main__":
    channel = 'my_channel'
    message = 'Hello, Redis Pub/Sub!'
    publish_message(channel, message)


# Subscribe to a channel
# pubsub = client.pubsub()
# pubsub.subscribe('my_channel')

# # Listen for messages
# for message in pubsub.listen():
#     if message['type'] == 'message':
#         print(f"Received message: {message['data'].decode('utf-8')}")