try:
    first_name = str(input("What is your name?: "))
    age = int(input("What is your age?: "))
    if 1>= age <=12:
        print("Children")
    elif 13 >= age <= 19:
        print("Teenager")
    else:
        print("Adult")

    color = str(input("What is your favourite colour?: "))
    home_town = str(input("Where is your home town?: "))

    profile = (first_name, age, color, home_town)
    print(f"\n---Profile Information---\nFirst name: \t{first_name}\nAge: \t\t{age}\nColour:  \t{color}\nHometown: \t{home_town}")

except ValueError:
    print("Invalid input! Please enter a valid number for age.")

