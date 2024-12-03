What is a server?
A server is a computer system that provides services or resources to other devices, typically over a network. In this case, the server hosts the web application and database.
What is the role of the domain name?
A domain name is a human-readable address (e.g., www.foobar.com) that maps to an IP address (e.g., 8.8.8.8) to simplify user access to web services.
What type of DNS record is www in www.foobar.com?
The www record is a CNAME (Canonical Name) or A Record pointing to the IP address 8.8.8.8.
What is the role of the web server?
The web server (Nginx) handles incoming HTTP requests, serves static content (like HTML/CSS), and forwards dynamic requests to the application server.
What is the role of the application server?
The application server executes the business logic of the application, processes requests, and interacts with the database.
What is the role of the database?
The database stores and manages data, making it accessible to the application server when required.
What is the server using to communicate with the user’s computer?
The server uses the HTTP/HTTPS protocols as the medium to format and transfer data, while underlying technologies like TCP/IP handle the reliable delivery and routing of these communications.
Single Point of Failure (SPOF)
This means if the single server goes down, the entire website becomes unavailable.
Downtime during maintenance
Restarting the web server or deploying updates will make the site temporarily inaccessible.
Scalability
The system cannot handle increased traffic as there is only one server, leading to potential overload.
