# Jace Conrad
# Chapter 6
# Stores information about multiple people in a list and prints everything we know about each person.

person_1 = {"first_name": "Marqus","last_name": "Hardin","age": 19,"city": "Ephrata",}

person_2 = {"first_name": "Soid", "last_name": "Orangeburg", "age": 19,"city": "South Carolina",}

person_3 = {"first_name": "Sam", "last_name": "Plaza","age": 18, "city": "Lancaster",}

person_4 = {"first_name": "Iven","last_name": "Johnson-Thompson", "age": 19,  "city": "Lancaster",}

people = [person_1, person_2, person_3, person_4]

for person in people:
  print(person["first_name"])
  print(person["last_name"])
  print(person["age"])
  print(person["city"])
  print()