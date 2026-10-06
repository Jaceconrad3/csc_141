# Jace Conrad
# Chapter 6
# Stores information about different cities in a dictionary and prints it out.

cities = {"philadelphia": {"country": "united states","population": "1.5 million","fact": "home of the liberty bell",},
"rome": {"country": "italy","population": "2.8 million","fact": "home of the colosseum",},
"paris": {"country": "france","population": "2.1 million","fact": "home of the eiffel tower",},}

for city, info in cities.items():
  print(city.title())
  print(info["country"].title())
  print(info["population"])
  print(info["fact"])
  print()