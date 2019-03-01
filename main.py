# ------------ Terminal-based Social Media DM Platform: Main File --------------

# Import functions from other files
from login import *
from pychatkit import *

# Clear the screen
clear()

# Log user in
login()

# Create or join a room?
op = input("Enter C to create a room or J to join a room: ")

# Clear screen
clear()

# If creating...
if op == "C":
    # Get room name and connect
    roomname = input("Name your room: ")
    createroom(roomname, [login.usern])

# If not creating...
else:
    # Get room name and connect
    roomname = input("Name of the room you want to join: ")
    joinroom(roomname, [login.usern])
