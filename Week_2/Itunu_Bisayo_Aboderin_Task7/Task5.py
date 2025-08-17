
# **Task5: Contact Quick Lookup**
# - Store three names and their phone numbers in two separate tuples.

#   - Create a dictionary from them using `dict(zip(...))`.

#   - Ask the user for a name and display the corresponding number (or an error message).

# - Requirements:

#   - Use `zip()` and d`ict()` to combine tuples.

#   - Use `.get()` for safe retrieval.

#   - No loops.

names = ("Ademola", "Adetola", "Ololade")
phone_no = ("8132456786", "7057628931", "9020456789")
phone_book = dict(zip(names, phone_no))
phone_name = input("Enter a name to find the phone no: ")
phone_search = phone_book.get(phone_name, "Name not found")
print(phone_search)