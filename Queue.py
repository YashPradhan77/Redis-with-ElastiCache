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
    host = 'PRIMARY-ENDPOINT'
    port = 6379

    queue = RedisQueue(host, port)
    
    # Enqueue messages
    queue.enqueue('my_queue', 'message')
    queue.enqueue('my_queue', 'message_fail')
    
    # Process messages
    queue.process_message('my_queue', 'my_dlq')
    queue.process_message('my_queue', 'my_dlq')
