text = input("Enter the text you wish to test: ")
letter = input("Enter the letter you wish to search for and count: ")
count = 0

for char in text:
    if char == letter:
        count += 1

print("The letter '", letter, "' appears ", count, " times in the text.")
#Capital and lowercase are treated as different letters.
