# **Task2: Unique Name Collector**
#  - Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.

name = str(input("What is your name?: "))
list_of_names = name.split()
list_of_name = set(list_of_names)
seminar_attendee = list(list_of_name)
seminar_attendee.sort()
print(seminar_attendee)

