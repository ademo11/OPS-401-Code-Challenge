# !/usr/bin/env python3
# Script: OPS 401 Class 02 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 1 May 2023
# Purpose: Ops Challenge: Network Security Tool with Scapy Part 2 of 3

import sys
import ipaddress
from scapy.all import *


def display_menu():
    print("Network Security Tool")
    print("1. TCP Port Range Scanner")
    print("2. ICMP Ping Sweep")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")
    return choice


def tcp_port_range_scanner():
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


def get_ip_list_from_cidr(cidr_block):
    network = ipaddress.ip_network(cidr_block, strict=False)
    ip_list = list(network.hosts())
    return ip_list


def ping_host(ip_address):
    icmp_response = sr1(IP(dst=str(ip_address))/ICMP(), timeout=2, verbose=0)
    
    if icmp_response is None:
        return "down"
    elif icmp_response.haslayer(ICMP):
        icmp_type = icmp_response.getlayer(ICMP).type
        icmp_code = icmp_response.getlayer(ICMP).code
        if icmp_type == 3 and icmp_code in [1, 2, 3, 9, 10, 13]:
            return "blocking"
        else:
            return "up"
    else:
        return "down"


def icmp_ping_sweep(ip_list):
    online_hosts = 0
    for ip_address in ip_list:
        status = ping_host(ip_address)
        if status == "up":
            print(f"{ip_address} is responding.")
            online_hosts += 1
        elif status == "down":
            print(f"{ip_address} is down or unresponsive.")
        elif status == "blocking":
            print(f"{ip_address} is actively blocking ICMP traffic.")
    print(f"\n{online_hosts} hosts are online.")


def main():
    while True:
        user_choice = display_menu()

        if user_choice == "1":
            tcp_port_range_scanner()
        elif user_choice == "2":
            cidr_block = input("Enter the network address with CIDR block (e.g., 10.10.0.0/24): ")
            ip_list = get_ip_list_from_cidr(cidr_block)
            icmp_ping_sweep(ip_list)
        elif user_choice == "3":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

