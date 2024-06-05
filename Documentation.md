# Redis With ElastiCache Implementation Documentation

dummy python code for all use case scenario of Redis Streams , Queues and Redis Cache purpose using ElastiCache Redis 

Such as

1. Pub/Sub

2. Queue

3. Caching

4. DLQ management

# Implementation

1. Create an ElastiCache Redis Cluster 

→ Configure your cluster by setting the name, node type, number of replicas, and other necessary parameters.

2. Configure Security group 

→ Add Inbound Rules for Port 6379

3. Create application instance in the same vpc and security group

→ ssh to instance and setup python environment

-> install python3 , pip , redis

4. Obtain Primary Endpoint from Redis Cluster

5. Then run the python scripts as follows: 

# For Caching 

Redis can be used as a caching layer to store frequently accessed data.
Redis uses the 'set' & 'get' commands to store and retrieve data
Where the 'Set' command obtains the data and stores it as a key-value pair to be rendered whenever 'get' command is given.

Code: Caching.py
```
import redis

redis_client = redis.StrictRedis(
    host='redis.eulx8y.ng.0001.use1.cache.amazonaws.com', 
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
    
```


The above code generates the following output:

![Screenshot 2024-06-05 135412](https://github.com/YashPradhan77/Redis-with-ElastiCache/assets/83752766/c6cabbff-7cf4-4b1d-bc1b-331412277186)

# For Pub/Sub 

Redis Pub/Sub allows for message broadcasting to multiple subscribers.
In redis Pub/Sub, You publish a message to a channel , and any subscriber to that channel will recieve the message

Code: Publish.py 
```
import redis
# Connect to ElastiCache Redis
client = redis.StrictRedis(host='rediscluster.eulx8y.ng.0001.use1.cache.amazonaws.com', port=6379, db=0)

# Publish a message
# client.publish('my_channel', 'Hello, Redis Pub/Sub!')
    
def publish_message(channel, message):
    client.publish(channel, message)
    print(f"Published message: {message} to channel: {channel}")

publish_message("my_channel","Hello")
```

![Screenshot 2024-06-05 144009](https://github.com/YashPradhan77/Redis-with-ElastiCache/assets/83752766/5d30704c-f96c-4954-a584-4c84680acb7b)

subscribe.py
```
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

```
Output:

![Screenshot 2024-06-05 143917](https://github.com/YashPradhan77/Redis-with-ElastiCache/assets/83752766/4624ff52-d906-43a7-a346-aa5a35b8b537)

In the following output , a user publishes a message to a channel , and another user who has subscriber to the channel will recieve the message

# For Queues & DLQ
In redis queues , a queue can be implemented using lists , a list will be automatically created when pushed an item onto it.
Redis lists are used to implement queues. The RPUSH and LPOP commands are typically used to enqueue and dequeue items respectively.

Code: queue.py 
```
import redis

class RedisQueue:
    def __init__(self, host, port, decode_responses=True):
        self.client = redis.StrictRedis(
            host=host,
            port=port,
            decode_responses=decode_responses
        )

    def enqueue(self, queue_name, item):
        self.client.lpush(queue_name, item)
        print(f"Enqueued: {item} to {queue_name}")

    def move_to_dlq(self, dlq_name, message):
        self.client.lpush(dlq_name, message)
        print(f"Moved to DLQ: {message}")
    
    def process_message(self, queue_name, dlq_name):
        message = self.client.rpop(queue_name)
        if message:
            print(f"Processing message: {message}")
            # Simulate a failure condition
            if "fail" in message:
                print(f"Error processing message: {message}, moving to DLQ")
                self.move_to_dlq(dlq_name, message)
            else:
                print(f"Message processed successfully: {message}")
        else:
            print("No messages to process")

# Usage example
if __name__ == "__main__":
    host = 'redis.eulx8y.ng.0001.use1.cache.amazonaws.com'
    port = 6379

    queue = RedisQueue(host, port)
    
    # Enqueue messages
    queue.enqueue('my_queue', 'message')
    queue.enqueue('my_queue', 'message_fail')
    
    # Process messages
    queue.process_message('my_queue', 'my_dlq')
    queue.process_message('my_queue', 'my_dlq')
```

Output:

![Screenshot 2024-06-05 145051](https://github.com/YashPradhan77/Redis-with-ElastiCache/assets/83752766/1f264271-63ca-4dab-a791-e0e2023b07e3)

Explanation:
In the following output , Incoming messages are first queued to be processed further . Once the messages are processed successfuly  , they are cleared from the queue . messages which show an error are not processed and are moved to DLQ(Dead letter Queue)
