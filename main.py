# ------------ Terminal-based Social Media DM Platform: Main File --------------

# Import functions from other files
from login import *
from clearscreen import *
from pychatkit import *

# Clear the screen
clear()

# Log user in
login()

# Print username
print(login.useraccount)

# Create or join a room?
op = input("Enter C to create a room or J to join a room: ")
# If creating
if op == "C":
    roomname = input("Name your room: ")
    createroom(roomname, [login.usern])
