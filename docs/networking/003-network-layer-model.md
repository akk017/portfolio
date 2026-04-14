---
title: networking layer model
date: 14-APR-2026
sources:[Beej's Networking Guide - Ch4](https://beej.us/guide/bgnet0/html/split/the-layered-network-model.html)
watch: true
---

#### Glossary

**<u>Bit</u>**: 1 or 0

**<u>Byte</u>**: 8 Bits or 1111 1111 or FF

**<u>IP Address</u>**: 4-byte number uniquely identifying your computer on the Internet.

<div>
<b><u>Port</u></b>:

Programs talk through ports, which are numbered 0-65535 and are associated with the TCP or UDP protocols.<br /><br/>

Since multiple programs can be running on the same IP address, the port provides a way to uniquely identify those programs on the network.
</div>
<p></p>

<div>
<b><u>TCP</u></b>:

Transmission Control Protocol, responsible for reliable, in-order data transmission. From a higher-up perspective, makes a packet-switched network feel more like a circuit-switched network. <br/><br/>

TCP uses port numbers to identify senders and receivers of data.
</div>
<p></p>

**UDP**: sibling of TCP, except lighter weight. Doesn’t guarantee data will arrive, or that it will be in order, or that it won’t be duplicated. If it arrives, it will be error-free, but that’s all you get.

**IPv6 Address**: 16 Bytes number to identifying your compute.

**NAT – Network Address Translation** A way to allow organizations to have private subnets with non-globally-unique addresses that get translated to globally-unique addresses as they pass through the router.


