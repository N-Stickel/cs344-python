def analyze_text(text):
    """Return text statistics for character count, word count, and lowercase e count."""
    return {
        "characters": len(text),
        "words": len(text.split()),
        "lowercase_e": text.count("e")
    }

if __name__ == "__main__":
    text = input("Enter a line or paragraph of text: ")
    stats = analyze_text(text)

    print(f"Characters (including spaces): {stats['characters']}")
    print(f"Words: {stats['words']}")
    print(f"Lowercase 'e' count: {stats['lowercase_e']}")
