# !/usr/bin/env python3
# Script: OPS 401 Class 02 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 19 April 2023
# Purpose: Ops Challenge: Uptime Sensor Tool Part 2 of 2

import smtplib
import datetime, time, os
from getpass import getpass

# Declare variable
up = "memphis won today"
down = "Lakers lost today"
last = 0
ping_result =0
email = input("please provide your email adress:")
password = getpass("please provide your password:")
ip = input("please provide the ip adress you are trying to monitor:")

# function to handle the up alert
def send_upalert():
    now = datetime.datetime.now()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email, password)
    message = "Memphis won game 2"
    s.sendmail("Lakersin6@lakerswon.com", email, message)
    s.quit()
    
#  function that handles the down alert
def send_downalert():
    
# function that does the ping test

def ping_test():
    if ((ping_result != last) and (ping_result == up)):
        last = up
        send_upalert()
    elif ((ping_result !=last) and (ping_result == up)):
        send_downalert()
        last = down

    response = os.system("ping -c +1 " + ip)
    if response == 0:
        ping_result = up
    else:
        ping_result = down

# infinite loop
while True:
    ping_test()
    time.sleep(2)
    
     
    
# Ask the user for an email address and password to use for sending notifications.

# Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).

# Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.

# References
## <https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151>
