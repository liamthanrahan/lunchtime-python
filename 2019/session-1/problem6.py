def sum_odd_numbers(n):
    _sum_of_numbers = 0
    for val in range(n):
        if (val % 2 == 1):
            _sum_of_numbers += val
    return _sum_of_numbers
