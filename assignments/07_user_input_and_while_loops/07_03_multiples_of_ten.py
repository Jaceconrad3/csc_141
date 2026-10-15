# Jace Conrad
# Chapter 7
# Tests whether a number you type in is a multiple of 10.
number = input("Enter a number, and I'll check if it's a multiple of 10 for you: ")
number = int(number)

if number % 10 == 0:
  print(f"Nice! {number} is definitely a multiple of 10.")
else:
  print(f"Nope, {number} isn't a multiple of 10.")