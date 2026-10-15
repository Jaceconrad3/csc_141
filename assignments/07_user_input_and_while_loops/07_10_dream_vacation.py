# Jace Conrad
# Chapter 7
# Surveys people about their dream travel destinations and saves everyone's answers.
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

print("\nPoll Results:")
for name, place in responses.items():
    print(f"{name} would like to visit {place}.")