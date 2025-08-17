# **Task1: Fruit collector**
# - Ask the user to enter 5 favourite fruits. Store them in a set and display the set.
fruit = str(input("Enter your 5 favourite fruits: " ))
fruit = fruit.split()
fruits = set(fruit)
print(fruits)
