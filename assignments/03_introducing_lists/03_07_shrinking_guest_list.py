guest= ["Kobe Bryant", "Jalen Hurts", "Michael Jordan", "Allen Iverson", "Tyrese Maxey", "VJ Edgecombe"]
print("I am sorry to inform you that my dinner table will not arrive in time, so I can only invite two people for dinner.")

popped_guest= guest.pop()
print (f" Dear {popped_guest}, I am sorry to inform you but you have been removed from dinner.")

popped_guest= guest. pop()
print( f" Dear {popped_guest}, I am sorry to inform you but you have been removed from dinner.")
popped_guest= guest. pop()
print( f" Dear {popped_guest}, I am sorry to inform you but you have been removed from dinner.")
popped_guest= guest. pop()
print( f" Dear {popped_guest}, I am sorry to inform you but you have been removed from dinner.")    

print (f" Dear {guest[0]}, you are still invited to dinner.") # Fixed: Changed 'ivited' to 'invited'
print (f" Dear {guest[1]}, you are still invited to dinner.")

del guest[0]
del guest [0]
print(f"final guest list: {guest}")

#Jace
#Conrad     
#this code removes guest then prints a message to the guest that they have been removed. Then the remaining guest get an invite.