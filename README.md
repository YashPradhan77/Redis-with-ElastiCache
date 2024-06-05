# Redis With ElastiCache

dummy python code for all use case scenario of Redis Streams and Redis Cache purpose using ElastiCache Redis

Such as

1. Pub/Sub

2. Queue

3. Caching

4. DLQ management

# Implementation

1. Create an ElastiCache Redis Cluster 

→ Set node type & Number of nodes

2. Configure Security group 

→ Add Inbound Rules for Port 6379

3. Create application instance in the same vpc and security group

→ ssh to instance and setup python environment

-> install pip , redis

4. Obtain Primary Endpoint from Redis Cluster

5. Then run the python script

# For Caching 

Redis uses the 'set' & 'get' commands to store and retrieve data
Where the 'Set' command obtains the data and stores it as a key-value pair to be rendered whenever 'get' command is given.
Code: Caching.py
![Screenshot 2024-06-05 105619](https://github.com/YashPradhan77/Redis-with-ElastiCache/assets/83752766/7eaab256-0aa6-481b-b2c4-b56889ce1a6d)
The above code generates the following output:

![Screenshot 2024-06-05 135412](https://github.com/YashPradhan77/Redis-with-ElastiCache/assets/83752766/c6cabbff-7cf4-4b1d-bc1b-331412277186)

# For Pub/Sub 
In redis Pub/Sub, You publish a message to a channel , and any subscriber to that channel will recieve the message
Code: publish.py , subscribe.py
![Screenshot 2024-06-05 143456](https://github.com/YashPradhan77/Redis-with-ElastiCache/assets/83752766/0e8ad6b0-aec1-40df-b71a-0cc577b2feee)
![Screenshot 2024-06-05 144009](https://github.com/YashPradhan77/Redis-with-ElastiCache/assets/83752766/582640cb-55a7-4fe4-be4d-5fafdb141501)

Output:

![Screenshot 2024-06-05 143917](https://github.com/YashPradhan77/Redis-with-ElastiCache/assets/83752766/4624ff52-d906-43a7-a346-aa5a35b8b537)
![Screenshot 2024-06-05 144009](https://github.com/YashPradhan77/Redis-with-ElastiCache/assets/83752766/5d30704c-f96c-4954-a584-4c84680acb7b)

In the following output , a user publishes a message to a channel , and another user who has subscriber to the channel will recieve the message

# For Queues & DLQ
In redis queues , a queue can be implemented using lists , a list will be automatically created when pushed an item onto it.
Code: queue.py 
Output:

![Screenshot 2024-06-05 145051](https://github.com/YashPradhan77/Redis-with-ElastiCache/assets/83752766/1f264271-63ca-4dab-a791-e0e2023b07e3)

Explanation:
In the following output , Incoming messages are first queued to be processed further . Once the messages are processed successfuly  , they are cleared from the queue . messages which show an error are not processed and are moved to DLQ(Dead letter Queue)
