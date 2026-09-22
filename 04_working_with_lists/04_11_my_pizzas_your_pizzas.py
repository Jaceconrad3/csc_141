# Jace conrad
# Chapter 4
favorite_pizzas = ["buffalo chicken", "pepperoni", "meat lovers"]
friend_pizzas = favorite_pizzas[:]

# Adding a new pizza to each list
favorite_pizzas.append("bbq chicken")
friend_pizzas.append("hawaiian")

# print my pizzas
print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(pizza)

# printing my friends pizzas
    print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
