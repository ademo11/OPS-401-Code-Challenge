# !/usr/bin/env python3
# Script: OPS 401 Class 02 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 31 May 2023
# Purpose: Ops Challenge:  Signature-based Malware Detection Part 2 of 3
import os
import hashlib
import time

# Prompt the user for the file name and directory to search in
file_to_search = input("Enter the file name to search for: ")
directory = input("Enter the directory to search in: ")

# Initialize counts
files_searched = 0
hits_found = 0

def generate_md5(file_path):
    """Generate MD5 hash for a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Walk through each file in the directory
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        files_searched += 1
        complete_file_path = os.path.join(dirpath, filename)
        if filename == file_to_search:
            hits_found += 1
            md5_hash = generate_md5(complete_file_path)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(os.path.getmtime(complete_file_path)))
            file_size = os.path.getsize(complete_file_path)
            print(f"MD5 hash: {md5_hash}, Timestamp: {timestamp}, File size: {file_size}, File path: {complete_file_path}")

# Print out the final statistics
print(f"\nSearched {files_searched} files.")
print(f"Found {hits_found} instances of {file_to_search}.")

# Reference
## Uses OpenAI to fix bug