# def square(number):
#     return number**2
#
# def square_map(a_list):
#     return list(map(square, a_list))

def square_map(a_list):
    return [i**2 for i in a_list]

numbers = [1,2,3,5]

# print(square_map(numbers))
