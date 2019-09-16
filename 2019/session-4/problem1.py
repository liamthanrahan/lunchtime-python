def longest_line(file_path, split_char):
    with open(file_path, 'r') as input_file:
        lines = input_file.readlines()  # reads all lines in a file into a list of strings
        line_number = 0
        index = 1
        num_words = len(lines[0].split(split_char))
        for line in lines[1:]:
            length = len(line.split(split_char))
            if length >= num_words:
                num_words = length
                line_number = index
            index += 1

    return {u'line_number': line_number, u'num_words': num_words}


# print(longest_line('text.txt', ' '))
