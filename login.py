# --------- Terminal-based Social Media DM Platform: Login Function ------------

# Import clear screen function
from clearscreen import *
import time

def login():
    # Set variables for clean slate user account
    useracc = " "
    passacc = " "

    # Set variables for admin user account
    adminn = "Admin"
    adminacc = "admin"
    adminpass = "admin123"

    # Set exit code variable
    excode = 1

    # Loop
    while excode != 0:
        # New account or no?
        newacc = input("Do you want to create a new account? [Y/N] ")

        # Don't want to create a new account?
        if newacc == "N":
            # Get user input for username
            username = input("Enter username: ")

            # Code for admin
            if username == adminacc:
                # Ask for password
                password = input("Welcome admin. Enter password: ")

                # Access Granted (if you get the password right)
                while password != adminpass:
                    password = input("Try again: ")

                # Exit
                excode = 0

            # Code for user who registered
            elif username == useracc:
                # Ask for password
                print("Welcome " + username + ". Enter your password: ")
                password = input()

                # Access Granted (if you get the password right)
                while password != passacc:
                    password = input("Try again: ")

                # Exit
                excode = 0

            # Go back!
            else:
                print("Invalid. Please try again... \n")
                excode = 1

        # Wanna create an account? Sure no problem!
        else:
            # Create temporary passwords
            pass1 = ""
            pass2 = " "
            # Get user's username
            usern = input("Enter name: ")
            useracc = input("Enter new username: ")

            # Get user's password and verify it
            while pass1 != pass2:
                pass1 = input("Enter your password: ")
                pass2 = input("Verify your password: ")

            # Go back!
            passacc = pass1
            excode = 1
            clear()

    # Access Granted!
    print("Access Granted")

    # Clear screen
    time.sleep(5)
    clear()

    # Set function attributes for user account and admin account
    login.useraccount = useracc
    login.usern = usern
    login.adminaccount = adminacc
    login.adminn = adminn
