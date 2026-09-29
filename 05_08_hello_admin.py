# Jace
# Conrad
# Chapter 5
# Uses lists, for loops, and if statements to print out special message. 
# One goes to admin and the rest go to the other users with a different message.
usernames = ['admin', 'soid', 'marq', 'ryan', 'steven', 'sam']

# Loop through the list and print a greeting to each user about 2K27
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you please fix your game and the 2K27 servers?")
    else:
        print(f"Hello {username.title()}, It's double rep in the rec! Ready to run some games on 2K27?")
