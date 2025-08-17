# **Task 5: Student Score Tracker**

# - Ask the user for 3 student names.

# - For each student, ask for their score.

# - Store the results in two lists (one for names, one for scores).

# - Print a formatted output showing Name — Score, aligned neatly.
#   - Tips: You are to start by creating two empty lists.

names = []
scores = []
for i in range(3):
    name = input(f"Enter name of student {i+1}: ")
    score = int(input(f"Enter score for {name}: "))

    names.append(name)
    scores.append(score)
print("\nStudent Results: ")
print("{:<15} {:<5}".format("Name", "Score"))  
print("-" * 20)

for i in range(3):
    print("{:<15} {:<5}".format(names[i], scores[i]))
