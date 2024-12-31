def word_count(text):
    words = text.split()
    return f"{len(words)} words found in the document"

def char_counts(text):
    chars = {}
    for char in text.lower():
        chars[char] = chars.get(char, 0) + 1

    return dict(sorted(chars.items(), key=lambda x: x[1], reverse=True))

def main():
    path = "books/frankenstein.txt"

    print("--- Begin report of {path} ---\n")

    with open(path) as f:
        book = f.read()
        print(word_count(book), "\n")
        for char, count in char_counts(book).items():
            if (char.isalpha()):
                print(f"The '{char}' character was found {count} times.")

    print("\n--- End report ---\n")

main()
