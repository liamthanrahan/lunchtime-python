def build_triangle(n):
    # place your code here
    triangle = ''
    for index in range(1, n + 1):
        if (index > 1):
            triangle += '\n'
        triangle += '*' * index
    return triangle


# print(build_triangle(5))
