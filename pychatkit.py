# --------- Terminal-based Social Media DM Platform: ChatKit Functions ---------

# Create room function
def createroom(name, user_ids):
    # Import system module
    from os import system

    # Send JSON request
    _ = system("curl -X POST \ https://us1.pusherplatform.io/services/chatkit/v1/e1c22924-0714-4eea-8319-2653dc35e1f9/rooms \ -d '{'name: '" + name + ", 'user_ids': " + str(user_ids) + "}' ")
