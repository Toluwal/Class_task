
# **Task 4: Name Organizer**
# - Ask the user to enter 5 names (separated by spaces).

# - Convert all names to lowercase.

# - Sort the list alphabetically.

# - Display them one name per line.
#   -Tips: use `range()`,`sort()`, `for`, `in`, `split()`, `len()`,`lower()` 

name = (input("Give five names in JSS3: "))
names = name.split(" ")
for i in range(len(names)):
    names[i] = names[i].lower()
names.sort()
print("\nSorted Names: ")
for i in range(len(names)):
    print(names[i])