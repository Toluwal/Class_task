# **Task4: Unique Members Registration**
# - Ask the user to enter three names separated by commas.

#    - Convert them to a set to ensure uniqueness.

#    - Create a dictionary where each name is a key and its length is the value.

# - Requirements:

#    - Use `.split(",")` and `set()` to remove duplicates.

#    - Use dictionary comprehension `{name: len(name) for name in set_of_names}`.
names = input("Enter three names: ")
list_of_names = set(names.split(","))
dict = {name.strip: len(name.strip()) for name in list_of_names}
print("dict:", list_of_names)

