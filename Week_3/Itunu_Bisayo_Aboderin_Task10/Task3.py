
names = ("Ademola", "Adetola", "Ololade")
phone_no = ("8132456786", "7057628931", "9020456789")
phone_book = dict(zip(names, phone_no))
try:
    phone_name = input("Enter a name to find the phone no: ")
    phone_search = phone_book[phone_name]
    print(phone_search)
except KeyError:
    print("Name not found")

    print("\nPhone Book: ")
    for key, value in phone_book.items():
        print(f"{key}: {value}")
