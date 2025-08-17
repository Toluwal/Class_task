# **Task1: Student Bio Data Storage**

# - Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary.

#   - Courses should be stored as a list.

#   - Display the bio-data neatly using escape sequences.

# - Requirements:

#   - Use `input()` to collect details.

#   - Use dictionary operations `(dict[key] = value)` to store data.

#   - Use `print()` formatting with `\n` and `\t` for better output.

student_info = {}
s_name = str(input("name of student: "))
s_age = int(input("age of student: "))
s_gender = str(input("gender of student: "))
s_courses = str(input("student course: "))

student_info = dict(name=s_name, age=s_age, gender=s_gender, )
courses = list(s_gender)

print(f"Student biodata information: \nName: \t\t{s_name}\nAge: \t\t{s_age} years old\nGender: \t{s_gender}\nCourses: \t{s_courses}") 

