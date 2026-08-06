import string

filename = input("Enter the name of the text file you wish to test (example: test_file.txt): ")

short_words = 0
medium_words = 0
long_words = 0
total_words = 0

try:
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()

        for word in words:
            length = len(word)
            total_words += 1

            if 1 <= length <= 3:
                short_words += 1
            elif 4 <= length <= 6:
                medium_words += 1
            else:
                long_words += 1

    print("\nWord Length Report")
    print("\n")
    print(f"Total words: {total_words}")
    print(f"Short words (1-3 characters): {short_words}")
    print(f"Medium words (4-6 characters): {medium_words}")
    print(f"Long words (7+ characters): {long_words}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
