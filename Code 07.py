import os
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def process_file(file_path, key, mode):
    with open(file_path, 'rb') as file:
        data = file.read()
    
    f = Fernet(key)
    processed_data = f.encrypt(data) if mode == 'encrypt' else f.decrypt(data)
    
    with open(file_path, 'wb') as file:
        file.write(processed_data)

def process_folder(folder_path, key, mode):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            process_file(file_path, key, mode)

def main():
    if not os.path.exists("key.key"):
        write_key()

    key = load_key()
    mode = input("Select mode:\n1. Encrypt a folder\n2. Decrypt a folder\n")
    folder_path = input("Enter folder path: ")

    if mode == '1':
        process_folder(folder_path, key, 'encrypt')
    elif mode == '2':
        process_folder(folder_path, key, 'decrypt')
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()

# Reference
## <https://www.pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-1/>
## <Python: List Of Files In Directory And Subdirectories>