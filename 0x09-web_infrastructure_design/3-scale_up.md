Additions to the Infrastructure
One Additional Server
Separating the Web Server, Application Server, and Database Server onto their own dedicated servers to improve scalability and maintainability.
Reason for Addition
Isolating these roles ensures that issues in one service (e.g., web server) do not impact the others.
Each layer can now scale independently based on resource needs.
1 load-balancer (HAproxy) configured as cluster with the other one
The purpose is configuring a second HAProxy instance to create a clustered setup.
Reason for Addition HAproxy
Ensures high availability of the load-balancing layer.
If one HAProxy instance fails, the other continues to handle traffic, preventing downtime.
Split components (web server, application server, database) with their own server
Web Server
Handles static content (HTML, CSS, JavaScript) and forwards dynamic requests to the Application Server.
Application Server
Processes business logic and interacts with the database for data.
Database Server
Stores and retrieves persistent data. Configured separately for performance and security.
