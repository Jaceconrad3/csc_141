# Jace Conrad
# Chapter 6
# Checks who has taken the favorite languages poll and invites new people.

favorite_languages = {"jen": "python", "sarah": "c","edward": "ruby","phil": "python",}

people_to_poll = ["jen", "jace", "sarah", "marqus", "edward"]

for person in people_to_poll:
  if person in favorite_languages:
    print(f"Thank you for taking the poll, {person.title()}!")
  else:
    print(f"{person.title()}, please take our favorite languages poll!")