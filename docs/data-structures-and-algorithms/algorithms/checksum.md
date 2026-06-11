---
title: Checksum
sources: >-
  [Beej's Netwokring](https://beej.us/guide/bgnet0/html/split/the-internet-protocol-ip.html)
  [Wiki](https://en.wikipedia.org/wiki/Longitudinal_redundancy_check)
date: 21-ARP-2025
watch: true

---

Error detection is a crucial process in data communication, ensuring the integrity and reliability of data transmitted across networks. In any communication system, data can be corrupted by factors like noise, interference, signal degradation, or hardware malfunctions. 

These errors can lead to data loss, misinterpretation, or failure of critical applications.

To address these challenges, error detection methods are used to identify errors in transmitted data and prompt corrective actions, such as retransmission.

Common error detection techniques include Vertical Redundancy Check (VRC), Longitudinal Redundancy Check (LRC), Cyclic Redundancy Check (CRC), and Checksum. 

### LRC

```
lrc := 0
for each byte b in the buffer do
    lrc := (lrc + b) and 0xFF
lrc := (((lrc XOR 0xFF) + 1) and 0xFF) // Parity Bit Added to Each TCP Segment
```

### VRC

