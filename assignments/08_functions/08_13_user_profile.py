# Jace Conrad
# Chapter 8
# Dif 5/10
users = {'jconrad': {'first': 'jace','last': 'conrad','trait_one': 'disciplined','trait_two': 'hardworking',
'trait_three': 'genuine',},}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    
    full_name = f"{user_info['first']} {user_info['last']}"
    traits = f"{user_info['trait_one']}, {user_info['trait_two']}, {user_info['trait_three']}"
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tTraits: {traits.title()}")