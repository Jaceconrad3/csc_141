# Jace
# Conrad
# Chapter 5
# Checks if new usernames are available by comparing them case-insensitively with current users.
current_users = ['admin', 'soid', 'marq', 'ryan', 'steven']
new_users = ['SAM', 'SOID', 'jace', 'eric', 'MARQ']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. You will need to enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")