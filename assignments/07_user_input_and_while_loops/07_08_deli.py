# Jace Conrad
# Chapter 7
# Processes a list of sandwich orders one by one and moves them over to a finished pile.
sandwich_orders = ["tuna", "turkey", "roast beef", "grilled cheese"]
finished_sandwiches = []


while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")