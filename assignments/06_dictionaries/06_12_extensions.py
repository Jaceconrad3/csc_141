# Jace Conrad
# Chapter 6
# Stores info from 6.8 in single-line dictionaries and prints all of the stored info
# Added 2 more pets to the list and printed out all of the info for each pet.
# Also added in the breed to the glossary

pet_1 = {"pet_name": "Moses", "animal": "Dog", "owner": "Steve Conrad", "breed": "Golden Doodle"}
pet_2 = {"pet_name": "Adonnis", "animal": "Dog", "owner": "Shereen Conrad", "breed": "Golden Doodle"}
pet_3 = {"pet_name": "Kiki", "animal": "Cat", "owner": "Jace Conrad", "breed": "Tabby"}
pet_4 = {"pet_name": "Tokyo", "animal": "Cat", "owner": "Sam Plaza", "breed": "Siamese"}
pet_5 = {"pet_name": "Dozer", "animal": "Dog", "owner": "Owen", "breed": "Bulldog"}
pet_6 = {"pet_name": "Luna", "animal": "Dog", "owner": "Josh", "breed": "Husky"}

pets = [pet_1, pet_2, pet_3, pet_4, pet_5, pet_6]

for pet in pets:
  print(f"My name is {pet['pet_name']}, and I am a {pet['breed']} {pet['animal']}. My owner is {pet['owner']}.")