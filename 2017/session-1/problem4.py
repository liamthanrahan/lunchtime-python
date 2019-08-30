# Ask the user to input a string. Return this string, with every character (char) repeated twice.
# e.g. ‘python’ should become ‘ppyytthhoonn’
# Use input() to test your program, but make sure you remove print statements and the input function when you submit

def double_char(word):
    word_with_repeated_chars = ""
    for c in word:
        word_with_repeated_chars += c + c
    return word_with_repeated_chars

# word = input("Enter some string: ")
# print(double_char(word))
