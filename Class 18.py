# !/usr/bin/env python3
# Script: OPS 401 Class 02 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 9 May 2023
# Purpose: Ops Challenge: Automated Brute Force Wordlist Attack Tool Part 3 of 3

import zipfile
import os

secret_message = "This is the secret message."

with open('secret.txt', 'w') as file:
    file.write(secret_message)



password = "your_password"
os.system(f"zip -P {password} secret.zip secret.txt")



def test_password(zip_file, password):
    try:
        zip_file.extractall(pwd=bytes(password, 'utf-8'))
        return True
    except:
        return False

def brute_force(zip_file_name, password_list_file):
    with zipfile.ZipFile(zip_file_name, 'r') as zip_file:
        with open(password_list_file, 'r') as pwd_file:
            for line in pwd_file:
                password = line.strip('\n')
                success = test_password(zip_file, password)
                if success:
                    print(f"Password found: {password}")
                    return password
    print("Password not found in the provided list.")
    return None

# call the brute_force function with the zip file name and the password list file
brute_force('secret.zip', 'rockyou.txt')
