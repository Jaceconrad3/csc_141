# Jace Conrad
# Chapter 6
# Stores favorite places for different people in a dictionary and prints them out.

favorite_places = {"steven": ["nashville", "louisiana", "philly"],
"jace": ["italy", "philly", "sea isle city nj"],"marqus": ["miami", "maryland"],}

for name, places in favorite_places.items():
  print(name.title())
  for place in places:
    print(place.title())
  print()