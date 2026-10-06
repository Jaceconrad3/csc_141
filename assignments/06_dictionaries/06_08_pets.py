# Jace Conrad
# Chapter 6
# Stores pet info in single-line dictionaries and prints everything we know about each pet.

pet_1 = {"pet_name": "Moses", "animal": "Dog", "owner": "Steve Conrad"}
pet_2 = {"pet_name": "Adonnis", "animal": "Dog", "owner": "Shereen Conrad"}
pet_3 = {"pet_name": "Kiki", "animal": "Cat", "owner": "Jace Conrad"}
pet_4 = {"pet_name": "Tokyo", "animal": "Cat", "owner": "Sam Plaza"}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
  print(pet["pet_name"])
  print(pet["animal"])
  print(pet["owner"])
  print()