# 6. Electricity Bill Formatter
#  - Ask for:
#    - Customer’s full name
#    - Units consumed (kWh) – integer
#    - Cost per unit – float
# - Calculate the total bill and print it in a neatly formatted receipt using escape sequences for line breaks.

full_name = input("Customer's fullname: ")
units_consumed = int(input("Units consumed (kwh): " ))
unit_cost = float(input("Cost per unit: "))
total_bill = units_consumed * unit_cost 
print(f"Electricity Bill Formatter\nTotal Bill is ₦{total_bill}k ")
