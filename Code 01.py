# !/usr/bin/env python3
# Script: OPS 301 Class 02 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 18 April 2023
# Purpose: Import libraries


# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# Evaluate the response as either success or failure.
# Assign success or failure to a status variable.
# For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.

import os
import time
from datetime import datetime

def ping_ip(ip_address):
    response = os.system("ping -c 1 " + ip_address)
    if response == 0:
        print("Lakers in 6")
    else:
        print("Memphis in 6")

    time.sleep(2)

    x = 2
    while x == 2:
        while True:
            print("Lakers in 6")

if __name__ == "__main__":
    VAR = "10.0.0.228"
    ping_ip(VAR)

    currentTime = datetime.now()
    print(currentTime)
