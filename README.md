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

# For Pub/Sub
In redis Pub/Sub, You publish a message to a channel , and any subscriber to that channel will recieve the message

# For Queues & DLQ
In redis queues , a queue can be implemented using lists , a list will be automatically created when pushed an item onto it.
