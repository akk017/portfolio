---
title: networking overview
date: 09-APR-2026
sources:[Beej's Networking Guide](https://beej.us/guide/bgnet0/html/split/networking-overview.html)
---

The network is hardware, and the OS controls all access to hardware. So if you want to write software to use the network, you have to do it through the OS.

Historically, and modernly, this was done using an API called the sockets API that was pioneered on Unix.

### 2.5 Protocols

Network Layers and Abstraction: 

1. A user program says, “I want to send the bytes ‘GET / HTTP/1.1’ to that web server over there.” (Servers are identified by IP address and a port on the Internet–more on that later.)

2. The OS takes the data and wraps it up in a header (that is, prepends some data) that provides error detection (and maybe ordering) information. The exact structure of this header would be defined by a protocol such as TCP or UDP.

3. The OS takes all of that, and wraps it up in another header that helps with routing. This header would be defined by the IP protocol.

4. The OS hands all that data to the network interface card (the NIC–the piece of hardware that’s responsible for networking).

5. The NIC wraps all that data up into another header that’s defined by a protocol such as Ethernet that helps with delivery on the LAN.

6. The NIC sends the entire, multiply-wrapped data out over the wire, or over the air (with WiFi).

This works well because each layer is responsible for different parts of the process. And since the layers don’t care what data is encapsulated below them, you can swap out protocols at various layers and still have the rest of them work.

`It’s a bit wrong to call them “Ethernet cables” because they are just wires, and Ethernet is a protocol`

