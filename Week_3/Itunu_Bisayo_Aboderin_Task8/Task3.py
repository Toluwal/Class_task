# - Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).

# - Start with an empty cart total (cart_total = 0).

# - Use assignment operators (+=) to add the price of some items into cart_total.

# - Print the list of items and the total price using an f-string like this:
# ```
# Items: ['Book', 'Pen', 'Bag']
# Total Price: ₦600


items = ["shoe", "clothes", "bag", "wrist-watch", "necklace", "wristband"]   # contains a list of items
price = [ 15000, 20500, 25000, 12000, 15000, 50000]                        # contains a list of prices of the items
cart_total = 0                     # Initialized total cart to be 0
cart_total += price[0]             # added the zeroeth item to cart total
cart_total += price[1]             # Added the first price
cart_total+= price[2]              # Added the second price
cart_total+=price[3]               # Added the third price
cart_total+=price[4]               # Added the fourth price
cart_total+=price[5]               # Added the fifth price

print(f"Items: {items}\nTotal price: ₦{cart_total}")        # Used f string to display items and cart total

# Output
# Items: ['shoe', 'clothes', 'bag', 'wrist-watch', 'necklace', 'wristband']
# Total price: ₦137500


