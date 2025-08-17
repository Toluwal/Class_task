# 9. Ask the user to enter a sentence and print the number of vowels in it.
vowels = "aeiouAEIOU"
country = str(input("Enter your country: "))
count = 0
for c in country:
    if c in vowels:
        count +=1
print(count)

