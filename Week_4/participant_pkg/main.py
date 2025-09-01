import csv
from pathlib import Path
from participant_pkg import file_ops 


workspace = Path('workspace_files')
workspace.mkdir(exist_ok=True)
path = workspace / "contact.csv"

partictipant_dict = {}

print("Participant Information Saver" .center(60, "-") )
while True:

    while True:
        try:
            name = input("Enter your name: ")
            if name == "":
                print("Name cannot be blank!")
                continue
            elif name.isdigit():
                print("Invalid input! Try again")
                continue
            else:
                partictipant_dict["Name"] = name
                break
        except Exception as e:
            print(f"Error{e}")

    while True:
        try:
            age = int(input("What is your age?: "))
            if age <= 0:
                print("Age should be whole number")
                continue
            else:
                partictipant_dict["age"] = age
                break
        except Exception as e:
            print("Invalid input!")
            continue
    while True:
        try:
            number = input("Enter your phone number: ")
            if len(number) != 11:
                print("Incomplete number, try again!")
                continue
            elif number.isalpha():
                print("Number cannot be alphabet")
            else:
                partictipant_dict["Number"] = number
                break
        except Exception as e:
                print("Invalid input!")
                continue
    while True:
        try:
            track = input("What is your course learning track?: ")
            if track == "":
                print("Invalid input! Enter the correct track.")
                continue
            elif track.isdigit():
                print("Track cannot be a number")
            else:
                partictipant_dict["Track"] = track
                break
        except Exception as e:
            print("Invalid input!")
            break

        choice = input("Do you want to add another information \n 1. No \n 2. Yes\nEnter: ")
        if choice == "1":
            print("Participant detail has been saved successfully.\n")
            break
        else:
            continue

    


        file_ops.save_participant(path, partictipant_dict)
        file_ops.load_participants(path)