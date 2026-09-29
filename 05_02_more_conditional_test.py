# Jace Conrad
# Chapter 5
# Equality and inequality with strings
qb = "hurts"
print("\nIs qb == 'hurts'? I predict True.")
print(qb == "hurts") 

print("\nIs qb == 'mahomes'? I predict False.")
print(qb == 'mahomes') 

print("\nIs qb != 'brady'? I predict True.")
print(qb != 'brady')


# Tests using lower() 
wr = 'SMITH'

print("\nIs wr.lower() == 'smith'? I predict True.")
print(wr.lower() == 'smith')

print("\nIs wr.lower() == 'SMITH'? I predict False.")
print(wr.lower() == 'SMITH')


# Numerical tests 
score = 50

print("\nIs score == 50? I predict True.")
print(score == 50)

print("\nis score != 50? I predict False.")
print(score != 50)

print("\nIs score > 40? I predict True.")
print(score > 40)

print("\nIs score < 60? I predict True.")
print(score < 60)

print("\nIs score >= 50? I predict True.")
print(score >= 50)

print("\nIs score <= 49? I predict False.")
print(score <= 49)


# Tests using and/or
jace = 20
steven = 27

print("\nIs jace >= 19 and steven >= 30? I predict False.")
print(jace >= 19 and steven >= 30)

print("\nIs jace < 30 and steven > 15? I predict True.")
print(jace < 30 and steven > 15)

print("\nIs jace >= 25 or steven >= 27? I predict True.")
print(jace >= 25 or steven >= 27)

print("\nIs jace > 25 or steven > 30? I predict False.")
print(jace > 25 or steven > 30)


# Items in a list or not in a list
big_mac = ['patties', 'pickles', 'cheese', 'bun', 'lettuce', 'sauce']

print("\nIs 'cheese' in big_mac? I predict True.")
print('cheese' in big_mac)

print("\nIs 'mayo' in big_mac? I predict False.")
print('mayo' in big_mac)

print("\nIs 'mayo' not in big_mac? I predict True.")
print('mayo' not in big_mac)
