countries= ["USA", "Canada", "France", "Germany"]
print("Original list:", countries)

print(f"number of countries: {len(countries)}")

countries[0]= 'Brazil(USA)'
print("Modified list:", countries)

countries.append("Canada")
print("After insert():", countries)

countries.insert(0, 'Mexico')
print("After insert():", countries)

del countries[1]
print( "After del:", countries)

popped_country = countries.pop()
print(f"Popped country: {popped_country}")
print("After pop():", countries)

countries.remove('Canada')
print("After remove():", countries)

print("Temporarily sorted:", sorted(countries))
print("Original list is safe:", countries)

countries.reverse()
print("After reverse():", countries)

countries.sort()
print("Permanently sorted (alphabetical):", countries)

countries.sort(reverse=True)
print("Permanently sorted (reverse alphabetical):", countries)





