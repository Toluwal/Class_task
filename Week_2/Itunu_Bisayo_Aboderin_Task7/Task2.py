# **Task2: Super Market Price List**
# - Create a program that stores items and their prices in a dictionary.

#   - Items should come from a list.

#   - Prices are entered by the user.

#   - Display all items and prices, then allow the user to update the price of an item.

# - Requirements:

#   - Use dictionary update method `.update()` or assignment.

#   - Use `.keys()` to display available items.

#   - Use input validation (no advanced functions).

items_list = ["Book", "Pen", "Pencil", "Eraser", "Ruler"]
prices = {}
print("input the price of the items")
for item in items_list:
     price = int(input(f"Enter the price for {item}?: "))
     prices[item] = price
print("\nItems and their prices: ")
for item, price in prices.items():
    print(f"{item}: {price}")
print("\nAvailable items to update:", list(prices.keys()))
update_item = input("Enter the item you want to update the price for: ")
new_price = int(input(f"Enter the new price for {update_item}: "))
prices.update({update_item: new_price})

print("\nUpdated items and their prices:")
for item, price in prices.items():
    print(f"{item}: {price}")

