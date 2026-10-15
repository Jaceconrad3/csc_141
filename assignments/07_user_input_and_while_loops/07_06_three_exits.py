# Jace Conrad
# Chapter 7
# Shows three different ways to stop a loop
# Conditional test in while
prompt = "Enter a topping (type 'quit' to finish): "
topping = ""
while topping != "quit":
    topping = input(prompt)
    if topping != "quit":
        print(f"Added {topping}!")


# Active variable
prompt = "Enter a topping (type 'quit' to finish): "
active = True
while active:
    topping = input(prompt)
    if topping == "quit":
        active = False
    else:
        print(f"Added {topping}!")


# Break statement
prompt = "Enter a topping (type 'quit' to finish): "
while True:
    topping = input(prompt)
    if topping == "quit":
        break
    print(f"Added {topping}!")