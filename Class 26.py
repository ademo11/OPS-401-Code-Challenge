# !/usr/bin/env python3
# Script: OPS 401 Class 02 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 1 May 2023
# Purpose: Ops Challenge: Select one of your Python tools created during this class so far that does not have a logging feature. On that tool:
# Add logging capabilities to your Python tool using the logging library.
# Experiment with log types. Build in some error handling, then induce some errors. Send log data to a file in the local directory.
# Confirm your logging feature is working as expected.
from scapy.all import *
import sys
import logging

# Set up logging
logging.basicConfig(filename='scapy_script.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# Port scanning function
def port_scan(ip):
    open_ports = []
    logging.info("Scanning ports...")

    try:
        for port in range(1, 1025):
            # if port == 500:  
                # raise Exception("Simulated error at port 500")
            pkt = IP(dst=ip)/TCP(dport=port, flags="S")
            response = sr1(pkt, timeout=1, verbose=0)

            if response is not None and response[TCP].flags == "SA":
                open_ports.append(port)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return

    if open_ports:
        logging.info("Open ports:")
        for port in open_ports:
            logging.info(f"\tPort {port}")
    else:
        logging.warning("No open ports found.")

# Function to perform an ICMP echo request (ping)
def ping_host(ip):
    icmp_request = IP(dst=ip)/ICMP()
    response = sr1(icmp_request, timeout=1, verbose=0)

    if response is None:
        logging.error("ICMP request failed")

    return response is not None

# Prompt the user for an IP address
target_ip = input("Enter the target IP address: ")

# Check if the host is responsive
logging.info("Pinging host...")
if ping_host(target_ip):
    logging.info("Host is responsive, proceeding with port scan.")
    port_scan(target_ip)
else:
    logging.error("Host is not responsive.")
