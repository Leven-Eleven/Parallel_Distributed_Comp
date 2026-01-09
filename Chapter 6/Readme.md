Pyro4 Server–Client Example

Server

The server is a Python program that allows other programs to call its functions over a network using Pyro4. It contains a class that has a method called `welcomeMessage`. This method receives a name from the client and returns a greeting message like “Hi welcome Ali”. The `@Pyro4.expose` decorator is used so that this method can be accessed remotely by clients.

To start the server, a Pyro4 daemon is created. This daemon listens for incoming client requests. The server object is registered with the daemon and then registered with the Pyro4 Naming Server using a name such as “server”. After registration, the server waits in a request loop and stays active to respond to clients.

Naming Server

The Pyro4 Naming Server works like a directory or phonebook. It stores the names of servers and their network addresses. Instead of the client knowing the exact address of the server, it simply asks the Naming Server for the server name.

The server uses `Pyro4.locateNS()` to connect to the Naming Server and register itself. The client also connects to the Naming Server to find the server using the same name. Before running the server or client, the Naming Server must be started using the command `pyro4-ns` and must remain running during communication.

Client

The client is the program that communicates with the server. It asks the user to enter their name and then connects to the server using a Pyro4 proxy with the name registered in the Naming Server. Once connected, the client calls the `welcomeMessage` method on the server and prints the greeting returned by the server.

To run the client successfully, the Naming Server and the server must already be running. After that, the client can be started and will receive a response from the server.

Celery Task Example

Overview

This example demonstrates how Celery is used to execute tasks asynchronously in a distributed system. Instead of running tasks immediately, Celery sends them to background workers using a message broker such as RabbitMQ.

The example task is a simple addition of two numbers. The task is sent to a Celery worker, which processes it independently and returns the result once completed.

Requirements

To run this example, Python 3 is required along with the Celery library, which can be installed using pip. A message broker such as RabbitMQ must also be installed and running. Other brokers like Redis can also be used.

Conclusion

This guide explains two different approaches to distributed computing using Python. Pyro4 is used for remote object communication where a client directly calls methods on a server. The Naming Server helps clients locate servers easily without hardcoding addresses. Celery, on the other hand, is used for distributed background task execution. Tasks are sent to workers through a message broker and processed asynchronously.

Both Pyro4 and Celery are useful for building scalable and efficient distributed systems. Pyro4 is suitable for remote procedure calls, while Celery is better for handling background and long-running tasks.
