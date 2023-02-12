"""Intro task 1
Secret PIN program
"""

secret_pin = ""
while not secret_pin:
    secret_pin = input("Enter your secret 4-digit PIN: ")
    if secret_pin == "0456":
        print("Your secret PIN is 0456")
        break
    else:
        print("You have entered in an incorrect PIN!")
