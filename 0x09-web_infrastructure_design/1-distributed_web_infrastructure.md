Load Balancer
Distributes incoming traffic to prevent overloading any single server, improving reliability and scalability.
Algorithm Used
Round-Robin Ensures traffic is distributed evenly across servers. Each request is sent to the next server in line.
The Load Balancer is enabling an Active-Active Setup where both servers handle traffic simultaneously.
This is different from Active-Passive Setup where One server is active, while the other is a standby backup.
Primary-Replica Database Cluster
The Primary Node (Master) handles write operations.
The Replica Node (Slave) asynchronously replicates data from the master, handling read operations.
Differences
The Primary node ensures data consistency during writes.
The Replica node offloads read operations for better performance.
Single Points of Failure (SPOF)
Load Balancer
If it fails, the entire system becomes inaccessible.
Database Server Without replication or clustering, failure results in data loss or unavailability
Security Issues
No Firewall
Open access exposes the infrastructure to attacks.
No HTTPS
Data exchanged between users and the servers is unencrypted, leading to potential data breaches.
No monitoring
Lack of monitoring means issues like server downtimes, high latencies, or security breaches may go unnoticed.
