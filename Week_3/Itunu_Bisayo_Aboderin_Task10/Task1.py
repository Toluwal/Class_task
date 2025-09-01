print("Welcome to Airtel USSD Service!")

code = "*123#"
pass_code = "4321"
amount = 2500

dial = input("Dial the USSD code: ")

if dial == code:
    while True:
        print("\nMenu:\n1. Check Balance\n2. Buy Airtime\n3. Buy Data\n4. Exit")
        choice = input("Enter your preferred option (1/2/3/4): ")

        if choice == "1":  # Check Balance
            password = input("Enter your password: ")
            if password == pass_code:
                print(f"Your balance is ₦{amount}")
            else:
                print("Invalid password! Try again.")

        elif choice == "2":  # Buy Airtime
            password = input("Enter your password: ")
            if password == pass_code:
                try:
                    airtime_choice = int(input("How much airtime do you want to purchase?: "))
                    if airtime_choice <= amount:
                        amount -= airtime_choice
                        print(f"You have successfully purchased ₦{airtime_choice} airtime.")
                        print(f"Your new balance is ₦{amount}")
                    else:
                        print("Insufficient balance.")
                except ValueError:
                    print("Invalid input! Please enter a number.")
            else:
                print("Invalid password! Try again.")

        elif choice == "3":  # Buy Data
            password = input("Enter your password: ")
            if password == pass_code:
                try:
                    data_choice = int(input("Enter amount to spend on data: "))
                    if data_choice <= amount:
                        amount -= data_choice
                        print(f"You have successfully purchased data worth ₦{data_choice}.")
                        print(f"Your new balance is ₦{amount}")
                    else:
                        print("Insufficient balance.")
                except ValueError:
                    print("Invalid input! Please enter a number.")
            else:
                print("Invalid password! Try again.")

        elif choice == "4":  # Exit
            print("Thank you for using Airtel USSD Service. Goodbye!")
            break

        else:
            print("Invalid input! Enter 1, 2, 3 or 4.")

else:
    print("Invalid input. Please enter the correct USSD code.")
