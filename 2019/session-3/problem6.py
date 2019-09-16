def square(num):
    return num * num


def square_map(a_list):
    squared_list = list(map(square, a_list))
    return squared_list


print(square_map([1, 2, 3]))
