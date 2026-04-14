---
title: sockets api
date: 14-APR-2026
sources:[Beej's Socket Guide](https://beej.us/guide/bgnet0/html/split/introducing-the-sockets-api.html)
---

In Unix, the sockets API generally gives processes a way to communicate with one another. It supports a variety of methods of communication, and one of those methods is over the Internet.

### 3.1 Client Connection Process

1. Ask the OS for a socket. In C, this is just a file descriptor (an integer) that will be used from here on to refer to this network connection. Python will return an object representing the socket. 

2. Perform a DNS lookup Convert human readble to machine readable.
3. Connect the socket to that IP address on a specific port.
4. Send data and receive data.
5. Close the connection.

### 3.2 Server Listening Process

1. Ask the OS for a socket.
2. Bind the socket to a port. 
programs that aren’t run as root/administrator can’t bind to ports under 1024–those are reserved.
3. Listen for incoming connections.
4. Accept incoming connections.
5. Send data and receive data.
6. Go back and accept another connection