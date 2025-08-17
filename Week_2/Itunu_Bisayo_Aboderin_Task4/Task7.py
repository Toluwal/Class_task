# **Task 7: List Manipulation**
# - Create a list of five cities.

# - Replace the third city with a new one (entered by the user).

# - Remove the last city.

# - Add a new city to the beginning of the list.

# - Print the updated list.
cities = ["Ikeja", "osogbo", "Ibadan", "Akure", "Abeokuta"]
new_city = str(input("Enter a new city: "))
cities[2] = new_city
city = cities.pop()
print(city)
print(cities)
cities.insert(0, "Ilorin")
print("\nUpdated list of cities: ", cities)  
