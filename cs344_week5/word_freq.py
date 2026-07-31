def count_words(text):
    """ Converts text to lowercase, splits test into words, and uses a dictionary to count how many times each word appears."""
    word_count = {}
    words = text.lower().split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

if __name__ == "__main__":
    test_text = input("Enter the text you wish to test: ")
    result = count_words(test_text)
    print("Word count:", result)