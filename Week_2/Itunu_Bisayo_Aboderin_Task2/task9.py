# 9. Nigerian Festival Info
#  - Ask for:
#      - Festival name (string)
#      - Location (string)
#      - Month held (string)
# - Display the info with quotation marks around the festival name using escape sequences `(\")`.

name = str(input("Festival name: "))
location = str(input("location: "))
month = str(input("Month held: "))
print(f"The {name} is an annual festival that takes place in {location} and usually in the month of {month}." )
