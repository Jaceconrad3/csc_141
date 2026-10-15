# Jace Conrad
# Chapter 7
# Cleans out all the pastrami orders from the list before making the rest of the sandwiches
sandwich_orders = ["pastrami","tuna","pastrami","turkey","roast beef","pastrami","grilled cheese",]
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami today!\n")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")