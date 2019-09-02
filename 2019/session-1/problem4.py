def double_char(word):
    word_with_repeated_chars = ''
    for char in word:
        word_with_repeated_chars += char + char
    return word_with_repeated_chars


# val = input("Gib me word: ")
# print(double_char(val))
