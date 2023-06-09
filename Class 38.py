# !/usr/bin/env python3
# Ops Challenge - XSS Vulnerability Detection with Python

## Demo Code

# Copy the demo code below to Web Security Dojo. Complete all TODOs.



#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: TODO: XSS Vulnerability Detection with Python
# Date:        TODO: 6/8/2023
# Modified by: TODO: Ademola Olatunbosun

### TODO: Install requests bs4 before executing this in Python3

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### TODO: Add function explanation here ###
def get_all_forms(url):
    # GET request to the website and convert the page to BeautifulSoup object
    soup = bs(requests.get(url).content, "html.parser")
    # find and return all form tags in the HTML content
    return soup.find_all("form")
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
#### Function to return all forms from the HTML content of a webpage

def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

### TODO: Add function explanation here ###
def get_form_details(form):
    details = {}
    # get the form action (target URL)
    action = form.attrs.get("action").lower()
    # get the form method (POST, GET, etc.)
    method = form.attrs.get("method", "get").lower()
    # get all the input details such as type and name
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
#### Function to return the details of a form including its method, action and inputs.



### TODO: Add function explanation here ###
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
#### Function to submit the form given in the form_details to the target URL with a value. 

def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

### TODO: Add function explanation here ###
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
#### Function to scan a website to check if it is XSS vulnerable.
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<Script>alert('hi')</Script>" ### TODO: Add HTTP and JS code here that will cause a XSS-vulnerable field to create an alert prompt with some text. This is a simple alert script in Javascript
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        ###  if the JS script is found in the response, then the form is vulnerable to XSS
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

### TODO: Add main explanation here ###
### This is the main entry point of the script
### In your own words, describe the purpose of this main as it relates to the overall objectives of the script ###
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

### TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### TODO: Test this script against one XSS-positive target 
# **Positive target output**: dojo@dojo-VirtualBox:~/Desktop/class-38$ python3 'new challenge.py'
# Enter a URL to test for XSS: https://xss-game.appspot.com/level1/frame
# [+] Detected 1 forms on  https://xss-game.appspot.com/level1/frame.
# [+] XSS Detected on  https://xss-game.appspot.com/level1/frame
# [*] Form details:
# {'action': '',
#  'inputs': [{'name': 'query',
#              'type': 'text',
#              'value': "<Script>alert('hi')</Script>"},
#             {'name': None, 'type': 'submit'}],
#  'method': 'get'}
# True
### and one XSS-negative target
# dojo@dojo-VirtualBox:~/Desktop/class-38$ python3 'new challenge.py'
# Enter a URL to test for XSS:http://dvwa.local/login.php
# [+] Detected 1 forms on http://dvwa.local/login.php.
# False
### TODO: Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection
