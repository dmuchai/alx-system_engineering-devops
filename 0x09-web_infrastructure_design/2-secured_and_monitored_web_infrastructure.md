Three Firewall Layers
Firewall 1 (Perimeter Layer)
Protects the Load Balancer from unauthorized access.
Allows only HTTPS traffic to reach the infrastructure.
Firewall 2 (Application Layer)
Restricts access to the Web Servers, permitting traffic only from the Load Balancer.
Firewall 3 (Data Layer)
Blocks all traffic to the Database Server except queries from the Web Servers.
1 SSL certificate to serve www.foobar.com over HTTPS
HTTPS ensures secure communication.
Monitoring Clients
Installed on all servers to collect performance metrics and logs.
Helps monitor, Web Server QPS (Query Per Second), Database query latency and uptime, Load Balancer traffic distribution and performance.
Sends data to tools like Sumo Logic, Datadog, or Prometheus for visualization and alerting.
Explain what to do if you want to monitor your web server QPS
To do this you need to set up a monitoring solution that collects, processes, and displays the relevant data.
Terminating SSL at the load balancer level is an issue because traffic between the Load Balancer and Web Servers is unencrypted, potentially exposing sensitive data in internal communications. Instead, use end-to-end encryption, maintaining HTTPS from the Load Balancer to the Web Servers.
Having only one MySQL server capable of accepting writes is an issue because it introduces a Single Point of Failure (SPOF). Database failure halts all write operations. Instead, implement Primary-Replica setup for high availability and failover support.
Having servers with all the same components (database, web server and application server) might be a problem because it complicates scaling and increases the impact of failures. Instead, separate roles into dedicated servers to ensure modularity and easier scaling.
