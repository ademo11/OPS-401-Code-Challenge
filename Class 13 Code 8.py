# !/usr/bin/env python3
# Script: OPS 401 Class 02 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 1 May 2023
# Purpose: Ops Challenge: Network Security Tool with Scapy Part 3 of 3
from scapy.all import *
import sys

# Port scanning function
def port_scan(ip):
    open_ports = []
    print("Scanning ports...")

    try:
        for port in range(1, 1025):
            pkt = IP(dst=ip)/TCP(dport=port, flags="S")
            response = sr1(pkt, timeout=1, verbose=0)

            if response is not None and response[TCP].flags == "SA":
                open_ports.append(port)

    except KeyboardInterrupt:
        sys.exit("\nExiting...")

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"\tPort {port}")
    else:
        print("No open ports found.")

# Function to perform an ICMP echo request (ping)
def ping_host(ip):
    icmp_request = IP(dst=ip)/ICMP()
    response = sr1(icmp_request, timeout=1, verbose=0)

    return response is not None

# Prompt the user for an IP address
target_ip = input("Enter the target IP address: ")

# Check if the host is responsive
print("Pinging host...")
if ping_host(target_ip):
    print("Host is responsive, proceeding with port scan.")
    port_scan(target_ip)
else:
    print("Host is not responsive.")



# References
## OpenAI
## 