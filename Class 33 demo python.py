# !/usr/bin/env python3
# Script: OPS 401 Class 02 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 31 May 2023
# Purpose: Ops Challenge:  Signature-based Malware Detection Part 3 of 3
# Python program to find the SHA-1 message digest of a file
# importing the hashlib module
# The below demo script works in tandem with virustotal-search.py from https://github.com/eduardxyz/virustotal-search, which must be in the same directory.
# Set your environment variable first to keep it out of your script here.


# import os

# apikey = os.getenv('API_KEY_VIRUSTOTAL') # Set your environment variable before proceeding. You'll need a free API key from virustotal.com so get signed up there first.
# hash = 'D41D8CD98F00B204E9800998ECF8427E' # Set your hash here. 

# # This concatenates everything into a working shell statement that gets passed into virustotal-search.py
# query = 'python3 virustotal-search.py -k ' + apikey + ' -m ' + hash

# os.system(query)

# import os

# os.environ['API_KEY_VIRUSTOTAL'] = 'your_api_key_here'

# apikey = os.getenv('API_KEY_VIRUSTOTAL') 
# hash = 'd50157f41fada50cade85284debf33aa642d02f1c01bab543c960861072d4561' 

# query = 'python3 virustotal-search.py -k ' + apikey + ' -m ' + hash

# os.system(query)

import hashlib
import os

# Fetch the API Key
os.environ['API_KEY_VIRUSTOTAL'] = 'your_api_key_here'
apikey = os.getenv('API_KEY_VIRUSTOTAL')

# Calculate the MD5 hash of the target file
def calc_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Your target file here
target_file = "/home/ademo11/OPS-401-Code-Challenge/virustotal-search-20230602-053042.txt"
hash = calc_md5(target_file)

# Create the query command
query = f'python3 virustotal-search.py -k {apikey} -m {hash}'

# Execute the query
os.system(query)
