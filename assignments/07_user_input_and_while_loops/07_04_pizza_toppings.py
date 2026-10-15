# Jace Conrad
# Chapter 7
# Keeps asking for pizza toppings in a loop until you type quit.
prompt = "Enter a pizza topping (type 'quit' when you're done): "
topping = " "
while topping != "quit":
  topping = input(prompt)
  if topping != "quit":
    print(f"Adding {topping} to your pizza!")