# !/usr/bin/env python3
# Script: OPS 401 Class 02 Ops Challenge Solution
# Author: Ademola
# Date of latest revision: 8 May 2023
# Purpose: Ops Challenge: Mode 1: Offensive; Dictionary Iterator, Mode 2: Defensive; Password Recognized

import time

def offensive_mode(rock_you_txt):
    with open(rock_you_txt, 'r') as f:
        for word in f:
            word = word.strip()
            print(word)
            time.sleep(1)

def defensive_mode(user_input, rock_you_txt):
    found = False
    with open(rock_you_txt, 'r') as f:
        for word in f:
            if word.strip() == user_input:
                found = True
                break
    if found:
        print("The string appeared in the word list.")
    else:
        print("The string did not appear in the word list.")

def main():
    mode = int(input("Select a mode (1: Offensive; Dictionary Iterator, 2: Defensive; Password Recognized): "))

    if mode == 1:
        rock_you_txt = input("Enter the path to the word list file: ")
        offensive_mode(rock_you_txt)
    elif mode == 2:
        user_input = input("Enter a string: ")
        rock_you_txt = input("Enter the path to the word list file: ")
        defensive_mode(user_input, rock_you_txt)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()


# References
## OpenAI