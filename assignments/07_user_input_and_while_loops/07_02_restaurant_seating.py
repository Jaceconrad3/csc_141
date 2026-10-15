# Jace Conrad
# Chapter 7
# Checks how many people are in your group to see if your table is ready or if you need to wait.
group_size = input("How many people are in your dinner group? ")
group_size = int(group_size)

if group_size > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")