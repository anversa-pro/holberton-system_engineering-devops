# DevOps
## Web Infrastructure Design

### Learning Objectives
*   You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
*   You must be able to explain what each component is doing
*   You must be able to explain system redundancy
*   Know all the mentioned acronyms: LAMP, SPOF, QPS

#### Task 0:
**You must be able to explain some specifics about this infrastructure:**  
*   What is a server
*   What is the role of the domain name
*   What type of DNS record www is in www.foobar.com
*   What is the role of the web server
*   What is the role of the application server
*   What is the role of the database
*   What is the server using to communicate with the computer of the user requesting the website
**You must be able to explain what the issues are with this infrastructure:**  
*   SPOF
*   Downtime when maintenance needed (like deploying new code web server needs to be restarted)
*   Cannot scale if too much incoming traffic

#### Task 1:
**You must be able to explain some specifics about this infrastructure:**  
*   For every additional element, why you are adding it
*   What distribution algorithm your load balancer is configured with and how it works
*   Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
*   How a database Primary-Replica (Master-Slave) cluster works
*   What is the difference between the Primary node and the Replica node in regard to the application
**You must be able to explain what the issues are with this infrastructure:**  
*   Where are SPOF
*   Security issues (no firewall, no HTTPS)
*   No monitoring

### Taks 2:
**You must be able to explain some specifics about this infrastructure:**  
*   For every additional element, why you are adding it
*   What are firewalls for
*   Why is the traffic served over HTTPS
*   What monitoring is used for
*   How the monitoring tool is collecting data
*   Explain what to do if you want to monitor your web server QPS
**You must be able to explain what the issues are with this infrastructure:**  
*   Why terminating SSL at the load balancer level is an issue
*   Why having only one MySQL server capable of accepting writes is an issue
*   Why having servers with all the same components (database, web server and application server) might be a problem

___________END___________