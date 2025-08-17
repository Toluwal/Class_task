# # 2. Price Display with Type Casting
# # Ask the user for the price of garri per paint in naira (as a string) and convert it to float. Display it with a message showing the amount in naira and kobo using print().

price = str(input("What is the price of gaari per paint in Naira: "))
float_price = float(price)
print(f"The price is ₦{float_price}k")

