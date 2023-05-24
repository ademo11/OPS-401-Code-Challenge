# !/usr/bin/env python3
# Script: OPS 401 Class 02 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 1 May 2023
# Purpose: Ops Challenge: Event Logging Tool Part 2 of 3

from scapy.all import *
import sys
import logging
from logging.handlers import TimedRotatingFileHandler

# Set up logging
log_file = 'scapy_script.log'
logger = logging.getLogger('ScapyLogger')
logger.setLevel(logging.DEBUG)

handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1)
handler.suffix = "%Y%m%d"
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

# Port scanning function
def port_scan(ip):
    open_ports = []
    logger.info("Scanning ports...")

    try:
        for port in range(1, 1025):
            # if port == 500:  
                # raise Exception("Simulated error at port 500")
            pkt = IP(dst=ip)/TCP(dport=port, flags="S")
            response = sr1(pkt, timeout=1, verbose=0)

            if response is not None and response[TCP].flags == "SA":
                open_ports.append(port)

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return

    if open_ports:
        logger.info("Open ports:")
        for port in open_ports:
            logger.info(f"\tPort {port}")
    else:
        logger.warning("No open ports found.")

# Function to perform an ICMP echo request (ping)
def ping_host(ip):
    icmp_request = IP(dst=ip)/ICMP()
    response = sr1(icmp_request, timeout=1, verbose=0)

    if response is None:
        logger.error("ICMP request failed")

    return response is not None

# Prompt the user for an IP address
target_ip = input("Enter the target IP address: ")

# Check if the host is responsive
logger.info("Pinging host...")
if ping_host(target_ip):
    logger.info("Host is responsive, proceeding with port scan.")
    port_scan(target_ip)
else:
    logger.error("Host is not responsive.") 

# References
## Uses OpenAI to fix bug