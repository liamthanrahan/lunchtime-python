def sum_multiples(n):
    total = 0
    for index in range(1, n):
        if (is_multiple(index)):
            total += index
    return total


def is_multiple(i):
    return i % 3 == 0 or i % 5 == 0


# print(sum_multiples(10))
