def longest_line(file_path, split_char):
    with open(file_path, 'r') as input_file:
        lines = input_file.readlines()
        line_number = 0
        num_words = len(lines[0].split(split_char))
        for line in lines[1:]:
            length = len(line.split(split_char))
            if length >= num_words:
                line_number = lines.index(line)
                num_words = length

    return {u'line_number': line_number, u'num_words': num_words}

# print(longest_line('longest_line.txt', ' '))
