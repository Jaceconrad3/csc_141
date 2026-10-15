# Jace Conrad
# Chapter 7
# Keeps asking for pizza toppings in a loop until you type quit.
pizzas = True
while pizzas:
  topping = input("What topping would you like on your pizza? (Type 'quit' to exit) ")
  if topping.lower() == 'quit':
    pizzas = False
  else:
    print(f"Great! We'll add {topping} to your pizza.")