# **Task6: Attendance Tracker**
# - Write a Python program that;

#  - Stores the days of the week in a tuple.

#  - Stores the months of the year in another tuple.

#  - Asks the user to enter:

#    - Student’s name

#    - Gender

#    - Course Track
   
#    - Current month number (1-12)

#    - Current day number (1-7)


weeks = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
months = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december")
student = str(input("What is your name?: "))
gender= str(input("What is your gender?: "))
course_track = str(input("Which course track did you enroll for?: "))
current_month_number = int(input("What is the current month number (1-12): "))
current_day_number = int(input("What is the current day number (1-7) ?: "))
print(weeks)
print(months)
print(f"Attendance tracker:\nweeks: \t\t\t{weeks}\nmonths: \t\t{months}\nstudent: \t\t{student}\ngender: \t\t{gender}\ncourse track: \t\t{course_track}\ncurrent month number: \t{months[current_month_number-1]}\ncurrent day number: \t{weeks[current_day_number-1]} ")