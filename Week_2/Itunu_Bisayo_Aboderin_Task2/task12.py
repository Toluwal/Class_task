# 12. Simulated USSD Menu Interaction
#  - You are to design a mock USSD interface for a mobile service.
#  - Requirements:
#    1. When the user runs the program, display a welcome screen with a Nigerian context greeting.
#    2. Ask the user to "dial" a USSD code (e.g., *123#) and store it in a variable.
#    3. Print a menu with at least 3 options (e.g., "Check Balance", "Buy Airtime", "Buy Data") using newline escape sequences `(\n)` for formatting.
#    4. Ask the user to choose an option (1, 2, or 3) and store their choice in a variable.
#    5. Use f-strings and/or concatenation to display a confirmation message showing the selected option.
#    6. Ask for an amount (if applicable) and store it as a number using type casting.
#    7. Display a final message summarizing the transaction

print("Welcome to GTB")
ussd_code = int(input(" dial ussd code: "))
Data_plans = str(input("1.Data plans\n2.Business plans\n3.Roaming/Int'l\n4.Borrow Credit/Recharge"))
DataPlans = "1"
BusinessPlans = "2"
Roaming = "3"
BorrowCredit= "4"
option = int(input("Enter your preferred option:"))
str(input("1. daily \n2. 2-3 Days\n3.Weekly\n4.Monthly"))
print(f"data plans: {Data_plans}\noption: {option}")
amount = int(input("amount: "))
print("Thank you for suscribing")