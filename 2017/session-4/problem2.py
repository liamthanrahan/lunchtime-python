def longest_string(words):
    longest_string_length = 0
    for word in words:
        if len(word) > longest_string_length:
            longest_string_length = len(word)
    return longest_string_length


def longest_line_string(file_path, split_char):
    with open(file_path, 'r') as input_file:
        lines = input_file.readlines()
        line_number = 0
        num_words = 0
        longest_string_length = 0
        for id, line in enumerate(lines):
            words = line.split(split_char)
            length = len(words)
            if length > num_words or (length == num_words and longest_string(words) >= longest_string_length):
                line_number = id
                num_words = length
                longest_string_length = longest_string(words)

    return {u'line_number': line_number, u'num_words': num_words, u'longest_string_length':longest_string_length}

# print(longest_line_string('longest_line.txt', ' '))
