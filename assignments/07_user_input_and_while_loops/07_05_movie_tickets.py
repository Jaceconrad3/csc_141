# Jace Conrad
# Chapter 7
# Figures out how much your movie ticket costs based on your age.
prompt = "Please enter your age (or type 'quit' to exit): "

while True:
  age_input = input(prompt)
  if age_input == "quit":
    break

  age = int(age_input)

  if age < 3:
    print("Your ticket is free!")
  elif age <= 12:
    print("Your ticket is $10.")
  else:
    print("Your ticket is $15.")