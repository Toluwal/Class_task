# name = input("What is your first name?: ")
# age = int(input("How old are you?: "))
# print(f" Welcome {name}, you are {age} years old.")

# price = input("What is the price of gaari?: ")
# float_price = float(price)
# print(f"The price of gaari in the market is #{float_price}k")

# dish = input("What is the name of a popular nigerian dish you know?: ")
# state = input("Which state is the Nigerian dish popular?: ")
# print(f"{dish} is a popular Nigerian dish.\n It is mostly eaten in \t{state} state.")

# name = input("What is the name of a major market in Abeokuta?: ")
# trader_no = int(input("How many traders are the market in a rough estimate?: "))
# revenue = float(input("What is the total revenue generated daily?: "))
# print(f"The popular {name} market in Abeokuta has a total number of {trader_no} traders and they generate a total revenue of #{revenue}k daily.")

# name = input("What is your full name?: ")
# units = int(input("What is the total unit of electricity consumed?: "))
# cost = float(input("What is the cost per unit: "))
# total_bill = units * cost
# print(f"-------June Electricity Bill -------\nCustomer name:\t\t{name}\nUnits Consumed: \t{units}\nUnit Cost: \t\t#{cost}k\nTotal Bill: \t\t#{total_bill}k")

# age = int(input("How old are you?: "))
# height = float(input("What is your height in metres?: "))
# name = input("What is your name?: ")
# print(f"My name is {name} and I am {age} years old with an average height of {height}m")

# distance = float(input("What is the total distance covered: "))
# fare = float(input("How much is the fare per km?: "))
# total_fare = distance * fare
# print(f"Total Fare: #{total_fare:.2f}k")

# name = input("What is the name of the festival happening soon?: ")
# location = input("Where will the festival be taking place?: ")
# month = input("Which month is the festival taking place?: ")
# print(f"The {name} festival is an annual festival in Yoruba land!\nThe Location of the festival is at {location}.\nThe festival will take place in the month of {month}.")

# naira_money = float(input("What is the total amount in naira?: "))
# dollar_rate = float(input("What is the exchange rate to US Dollars?: "))
# pound_rate = float(input("What is the exchange rate to pounds?: "))
# dollar_conversion = naira_money * dollar_rate
# pound_conversion = naira_money * pound_rate
# print(f"Amount in Naira\t Amount in USD\t Amount in pounds\n#{naira_money}\t${dollar_conversion}\t*{pound_conversion}")

# print("Welcome to Airtel USSD Service!")
# code = "*123#"
# pass_code = "4321"
# amount = 2500
# dial = input("dial the ussd code: ")
# if dial == code:
#     print(f"Menu: \n 1. Check balance\n2. Buy Airtime\n3. Buy data")
#     choice = input("Enter your preferred option 1/2/3: ")
#     if choice == "1":
#         print("1. Check balance")
#         password = input("Enter your password: ")
#         if password == pass_code:
#             print(f"Your balance is {amount}")
#         else: 
#             print("invalid input! Try again.")
#             if choice == "2":
#                 print("2. Buy Airtime")
#                 airtime_choice = input("How much airtime do you want to purchase?: ")
#                 amount-=airtime_choice
#                 if password == pass_code:
#                     print(f"You have successfully purchase{airtime_choice} airtime.")
#                 else:
#                     print("invalid input! Try again.")
#                     if choice =="3":
#                         print("3. Buy Data")
#                         data_choice = input("How much data do you want to buy?: ")
#                         if password == pass_code:
#                             print(f"You have successfully purchase{data_choice} data.")
#                         else: 
#                             print("invalid input! Try again.")
#                     else:
#                         print("invalid input! Enter the correct option.")       
#             else:
#                 print("invalid input! Enter the correct option.")  
#     else:
#         print("invalid input! Enter the correct option.")  
# else:
#     print("invalid input. Please enter the right code.")                  
                           

print("Welcome to Airtel USSD Service!")

code = "*123#"
pass_code = "4321"
amount = 2500

dial = input("Dial the USSD code: ")

if dial == code:
    print("Menu:\n1. Check Balance\n2. Buy Airtime\n3. Buy Data")
    choice = input("Enter your preferred option (1/2/3): ")

    if choice == "1":  # Check Balance
        password = input("Enter your password: ")
        if password == pass_code:
            print(f"Your balance is ₦{amount}")
        else:
            print("Invalid password! Try again.")

    elif choice == "2":  # Buy Airtime
        password = input("Enter your password: ")
        if password == pass_code:
            airtime_choice = int(input("How much airtime do you want to purchase?: "))
            if airtime_choice <= amount:
                amount -= airtime_choice
                print(f"You have successfully purchased ₦{airtime_choice} airtime.")
                print(f"Your new balance is ₦{amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid password! Try again.")

    elif choice == "3":  # Buy Data
        password = input("Enter your password: ")
        if password == pass_code:
            data_choice = int(input("Enter amount to spend on data: "))
            if data_choice <= amount:
                amount -= data_choice
                print(f"You have successfully purchased data worth ₦{data_choice}.")
                print(f"Your new balance is ₦{amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid password! Try again.")

    else:
        print("Invalid input! Enter 1, 2, or 3.")

else:
    print("Invalid input. Please enter the correct USSD code.")


# word = "Python"
# print(f"first character is {word[0]}")
# print(f"last character is {word[-1]}")

# name = input("What is your name?: ")
# print(f"Hello! {name}")

# character = "school"
# print(character.find(character[-1]))

# word = "Hello World"
# print(word.replace("World", "python"))

# text = "python programming language"
# print("python" in text)

# word = "school"
# reverse_word = "".join(reversed(word))
# print(reverse_word)
# print(f"The reversed word is {reverse_word}")

# sentence = "    The name of my school is Ladoke Akintola University of Technology   "
# print(sentence.strip())

# vowels = "AEIOUaeiou"
# sentence = input("Where do you live?:")
# count = 0
# for char in sentence:
#     if char in vowels:
#         count +=1
# print(count)

# number = int(input("Enter number 1234: "))
# result = number * 2
# print(result)

# fruits = "apple, banana, orange"
# print(f"Fruit list: {fruits.split()}")

# character = "Helmets"
# print(character.find(character[-1]))

# sentence = input("How old are you?: \n")
# print(sentence.split())
