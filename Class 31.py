# !/usr/bin/env python3
# Script: OPS 401 Class 02 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 30 May 2023
# Purpose: Ops Challenge:  Signature-based Malware Detection Part 1 of 3
#The script must successfully execute on both Ubuntu Linux 20.04 Focal Fossa and Windows 10. 
import os

# Prompt the user for the file name and directory to search in
file_to_search = input("Enter the file name to search for: ")
directory = input("Enter the directory to search in: ")

# Initialize counts
files_searched = 0
hits_found = 0

# Walk through each file in the directory
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        files_searched += 1
        if filename == file_to_search:
            hits_found += 1
            print(f"File found: {os.path.join(dirpath, filename)}")

# Print out the final statistics
print(f"\nSearched {files_searched} files.")
print(f"Found {hits_found} instances of {file_to_search}.")
