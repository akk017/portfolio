---
title: Internet Protocol
sources: [Beej's Netwokring](https://beej.us/guide/bgnet0/html/split/the-internet-protocol-ip.html)
date: 21-ARP-2025
---

This protocol is responsible for routing packets of data around the Internet, analogous to how the post office is responsible for routing letters around the mail network.

### Two Common Version

1. IPv4: 192.168.0.1 -> 4 Bytes
2. IPv6: fe80::c2b6:f9ff:fe7e:4b4 -> 16 Bytes

### Additional IP-layer Protocols

1. ICMP: Internet Control Message Protocol, a mechanism for communicating IP nodes to talk about IP control metadata with one another.
2. IPSec: Internet Protocol Security, encryption and authentication functionality. Commonly used with VPNs (Virtual Private Networks).

Users commonly interface with ICMP when using the ping utility. This uses ICMP “echo request” and “echo response” messages.

The traceroute utility uses ICMP “time exceeded” messages to find out how packets are being routed.

### Private Networks

There are private networks hidden behind routers that do not have globally unique IP addresses on their machines.

This is made possible because of **NAT(Network Address Translation)**

Big Endian -> Forward eg. 123
Little Endian -> Backward eg. 321

