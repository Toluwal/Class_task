
# week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday")
# activity = str(input("input activity for three days: "))
# selected_days = ("Tuesday", "Thursday", "Saturday")
# activities = []
# for day in selected_days:
#     activity = input(f"What activity do you want to do on {day}? ")
#     activities.append(activity)
# print(activities)
# activity_dict = {day: activity for day, activity in zip(selected_days, activities)}
# print("\nPlanned activities:")
# print(activity_dict)

# **Task3: Days and Activities Pairing**
# - Store days of the week in a tuple and ask the user to input an activity for three specific days.

#   - Use dictionary comprehension to pair days and activities.

#   - Print the dictionary.

# - Requirements:

#   - Use a tuple for days.

#   - Use {day: activity for day, activity in `zip(..., ...)`}.
#   Tip: Research on how to use `zip()`

week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
selected_days = ("Monday", "Thursday",  "Saturday")
activities = []
for day in selected_days:
     activity = input(f"Enter an activity for {day}: ")
     activities.append(activity)
day_activity = {day: activity for day, activity in zip(selected_days, activities)}
print("\nActivities for the selected  for the selected days: ")
print(day_activity)

