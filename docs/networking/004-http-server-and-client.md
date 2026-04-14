---
title: HTTP Server and Client
sources: [Beej's Netwokring](https://beej.us/guide/bgnet0/html/split/project-http-client-and-server.html)
sources: [C Linux Bind](https://linux.die.net/man/2/bind)
watch: true
---

A sample of code, connecting to socke

```python
import socket

# socket.socket(Family, TCP or UDP)
# Family
# AF_UNIX: Local / Inter Process Comunication
# AF_INET -> IPv4
# AF_INET6 -> IPv6
# 
# SOCK_STREAM -> TCP
# SOCK_DGRAM -> UDP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)

s.bind("/tmp/socket.sock")

while True:
    s.listen(1)
    print("\r\nblocking\r\n")
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode())
        conn.sendall(data)
    conn.close()
```

`s.accept()` is a blocking, will accept new connections.


### HTTP Hyper Text Transfer Protocol

HTTP operates on the concept of requests and responses.

A simple HTTP request from a client looks like this:

```
GET / HTTP/1.1
Host: example.com
Connection: close
```

A simple HTTP response from a server looks like:

```
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 6
Connection: close

Hello!
```

Ends-of-line are delimited by a Carriage Return/Linefeed combination. In Python or C, CRLF is"\r\n"

