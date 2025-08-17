# 10. School Fees Breakdown
#   - Ask for:
#     - School name
#     - Tuition fee (float)
#     - Hostel fee (float)
#     - Feeding fee (float)

# - Calculate the total and print it in receipt format with each fee on a new line.

name = str(input("School name: "))
fee = float(input("Tuition fee: "))
hostel= float(input("Hostel fee: "))
feeding =float(input("Feeding fee: "))
total =fee + hostel + feeding
print(f"School Fees Breakdown\nReceipt\nSchool name: {name}\nTuition Fee: ₦{fee: .2f}k/nHostel Fee: ₦{hostel: .2f}k\nFeeding Fee: ₦{feeding: .2f}k\nTotal payment: ₦{total: .2f}k")
