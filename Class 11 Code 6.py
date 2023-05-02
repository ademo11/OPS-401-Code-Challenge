# # !/usr/bin/env python3
# # Script: OPS 401 Class 02 Ops Challenge Solution
# # Author: Ademola
# # Date of latest revision: 1 May 2023
# # Purpose: Ops Challenge: Network Security Tool with Scapy Part 1 of 3
from scapy.all import ICMP, IP, sr1, TCP
import sys

# Define host IP
host = "scanme.nmap.org"
# Define port range or specific set of ports to scan
port_range = [22, 23, 80, 443, 3389]
# Test each port in the specified range using a for loop
filtered_ports = []

# Moved src_port variable outside the for loop
src_port = 1025

for dst_port in port_range:
    # Send the packet and wait for a response with a timeout of 1 seconds
    response = sr1(IP(dst=host) / TCP(sport=src_port, dport=dst_port, flags="S"), timeout=1, verbose=0)

    if response is None:
        # Changed variable 'port' to 'dst_port'
        filtered_ports.append(dst_port)
        print(f"Port {dst_port}: Filtered")
    elif response.haslayer(TCP):
        tcp_layer = response.getlayer(TCP)
        if tcp_layer.flags == 0x12:
            print(f"Port {dst_port}: Open")
        elif tcp_layer.flags == 0x14:
            print(f"Port {dst_port}: Closed")
    else:
        print(f"Port {dst_port}: Unknown response")




        

  
  # References
  ## <https://scapy.readthedocs.io/en/latest/index.html>
  ## <https://scapy.readthedocs.io/en/latest/introduction.html#>
