# **Task 6: Word Analyzer**
# - Ask the user to input a word.

# - Print the length of the word.

# - Check if it is all uppercase, all lowercase, or title case.

# - Reverse the word using slicing


word =str(input("Enter your favourite city: "))
print("Length of word: ", len(word))

if word.isupper():
    print("The word is in UPPERCASE.")
elif word.islower():
    print("The word is in lowercase.")
elif word.istitle():
    print("The word is in Title Case.")
else:
    print("The word has mixed case.")

print("Reversed word:", word[::-1])
