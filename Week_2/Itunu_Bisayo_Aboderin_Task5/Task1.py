# **Task1:  Create and Display**

# - Ask the user to enter three favorite Nigerian dishes (one at a time).

#  - Store them in a tuple called dishes.

# - Print the tuple in a single line, separating items with commas.

# - Use the \n escape sequence to print each dish on a new line.

dish1 = str(input("What is your most prefered favorite Nigerian dishes: "))
dish2 = str(input("What is your second most prefered favorite Nigerian dishes: "))
dish3 = str(input("What is your third most prefered favorite Nigerian dishes: "))
dishes = (dish1, dish2, dish3)
print(dishes)
print(f"My most favourite nigerian dish is: {dish1},\n followed by: {dish2},\n and lastly: {dish3}.")
