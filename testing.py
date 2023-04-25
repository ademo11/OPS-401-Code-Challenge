from cryptography.fernet import Fernet
import os

# Declare a function to write a key to a file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Declare a function to load a key from a file
def load_key():
    return open("key.key", "rb").read()

# Declare a function to encrypt a file
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

# Declare a function to decrypt a file
def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

# Declare a function to encrypt a string
def encrypt_string(cleartext, key):
    f = Fernet(key)
    ciphertext = f.encrypt(cleartext.encode())
    print(ciphertext.decode())

# Declare a function to decrypt a string
def decrypt_string(ciphertext, key):
    f = Fernet(key)
    cleartext = f.decrypt(ciphertext.encode())
    print(cleartext.decode())

# Declare the main function
def main():
    # Load the key from the file
    key = load_key()

    # Prompt the user to select a mode
    mode = input("Select mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n")

    # Execute the selected mode
    if mode == '1':
        file_path = input("Enter filepath to target file: ")
        encrypt_file(file_path, key)
    elif mode == '2':
        file_path = input("Enter filepath to target file: ")
        decrypt_file(file_path, key)
    elif mode == '3':
        cleartext = input("Enter cleartext string: ")
        encrypt_string(cleartext, key)
    elif mode == '4':
        ciphertext = input("Enter ciphertext string: ")
        decrypt_string(ciphertext, key)
    else:
        print("Invalid mode selected.")

# Call the main function
if __name__ == "__main__":
    main()
