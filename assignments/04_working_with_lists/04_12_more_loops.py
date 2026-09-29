# Jace conrad
# Chapter 4

my_foods = ['steak', 'lobster', 'pizza']
friend_foods = my_foods[:]

# This adds a new food to each list
my_foods.append('cannoli')
friend_foods.append('ice cream')

# uses for loop to print my new favorites
print("My favorite foods are:")
for food in my_foods:
    print(food)

# uses for loop to print my friends favorites
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)