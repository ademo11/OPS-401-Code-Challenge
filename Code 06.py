# # !/usr/bin/env python3
# # Script: OPS 401 Class 02 Ops Challenge Solution
# # Author: Ademola
# # Date of latest revision: 24 April 2023
# # Purpose: Ops Challenge: File Encryption Script Part 1 of 3
# # import librararies
# from cryptography.fernet import Fernet

# # Delare function

# # function to handle writing key

# # In Python, create a script that utilizes the cryptography library to:

# # Prompt the user to select a mode:
# # Encrypt a file (mode 1)
# # Decrypt a file (mode 2)
# # Encrypt a message (mode 3)
# # Decrypt a message (mode 4)
# # If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
# # If mode 3 or 4 are selected, prompt the user to provide a cleartext string.
# # Depending on the selection, perform one of the below functions. You’ll need to create four functions:
# # Encrypt the target file if in mode 1.
# # Delete the existing target file and replace it entirely with the encrypted version.
# # Decrypt the target file if in mode 2.
# # Delete the encrypted target file and replace it entirely with the decrypted version.
# # Encrypt the string if in mode 3.
# # Print the ciphertext to the screen.
# # Decrypt the string if in mode 4.
# # Print the cleartext to the screen.

from cryptography.fernet import Fernet
import os

# function to load the key

file_path = 'text.txt'

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

def encrypt_string(cleartext, key):
    f = Fernet(key)
    ciphertext = f.encrypt(cleartext.encode())
    print(ciphertext.decode())

def decrypt_string(ciphertext, key):
    f = Fernet(key)
    cleartext = f.decrypt(ciphertext.encode())
    print(cleartext.decode())

def main():
    key = Fernet.generate_key()
    mode = input("Select mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n")
    if mode == '1':
        file_path = input("Enter filepath to target file: ")
        encrypt_file(file_path, key)
    elif mode == '2':
        file_path = input("Enter filepath to target file: ")
        decrypt_file(file_path, key)
    elif mode == '3':
        cleartext = input("Enter ciphertext string: ")
        encrypt_string(cleartext, key)
    elif mode == '4':
        ciphertext = input("Enter ciphertext string: ")
        decrypt_string(ciphertext, key)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
