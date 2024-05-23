import redis

# Connect to the Redis server
client = redis.StrictRedis(host='rediscluster.eulx8y.ng.0001.use1.cache.amazonaws.com', port=6379, db=0)

def message_handler(message):
    if message['type'] == 'message':
        print(f"Received message: {message['data'].decode('utf-8')}")

if __name__ == "__main__":
    pubsub = client.pubsub()
    pubsub.subscribe('my_channel')
    
    print("Subscribed to 'my_channel'. Waiting for messages...")
    
    try:
        for message in pubsub.listen():
            message_handler(message)
    except KeyboardInterrupt:
        print("Unsubscribing and exiting...")
        pubsub.unsubscribe('my_channel')
