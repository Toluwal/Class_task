# 11. Nigerian Currency Converter (Very Advanced)
#   - Ask for:
#     - Amount in Naira (float)
#     - Exchange rate to US Dollars (float)
#     - Exchange rate to British Pounds (float)

# - Convert and print results with thousands separators and currency symbols, neatly aligned in a table-like format using escape sequences.
amount = float(input("Amount in Naira: "))
US_dollars = float(input("Exchange rate to US Dollars: ")) 
British_pounds = float(input("Exchange rate to British pounds: "))
print(f"Amount in Naira: \t\t₦{amount}, \nExchange rate to US Dollars: \t${US_dollars}, \nExchange rate to British Pounds:£{British_pounds}")

