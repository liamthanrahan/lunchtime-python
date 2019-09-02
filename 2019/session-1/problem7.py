def sum_div3_numbers(n):
    _sum_of_numbers = 0
    for val in range(n):
        if (val % 3 == 0):
            _sum_of_numbers += val
    return _sum_of_numbers
