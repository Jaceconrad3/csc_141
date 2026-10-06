# Jace Conrad
# Chapter 6
# Stores multiple favorite basketball numbers for each person in a dictionary and prints them.

favorite_numbers = {"ryan": [3, 24], "mya": [7, 32],"marqus": [24, 23],"soid": [67, 34],"jace": [23, 3],}

for name, numbers in favorite_numbers.items():
  print(name.title())
  for number in numbers:
    print(number)
  print()