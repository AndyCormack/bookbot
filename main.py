def word_count(text):
    words = text.split()
    return f"There are {len(words)} words in the book."

def char_counts(text):
    chars = {}
    for char in text.lower():
        chars[char] = chars.get(char, 0) + 1

    return chars

with open("books/frankenstein.txt") as f:
    book = f.read()
    print(word_count(book))
    print(char_counts(book))
