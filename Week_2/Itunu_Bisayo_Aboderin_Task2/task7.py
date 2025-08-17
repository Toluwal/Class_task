# 7. Mixing Data Types
#  - Ask the user for:
#     - Your age (integer)
#     - Your height in meters (float)
#     - Your name (string)
# - Print a sentence using f-string showing all details in one line, making sure you type-cast where necessary.

age = int(input("Your age: "))
height = float(input("Your height in meters: "))
name = str(input("Your name: "))
print(f"My {name} is and I am {age} years old and my height is {height}m.")
