# 8. Transport Fare Calculator
#  - Ask for:
#     - Distance in km (float)
#     - Fare per km (float)
# - Calculate and display the total fare with two decimal places using `f"{value:.2f}"`.

distance = float(input("Distance in km: "))
fare = float(input("Fare per km: "))
total_fare = distance * fare
print(f"The total fare is ₦{total_fare: .2f}k.")
