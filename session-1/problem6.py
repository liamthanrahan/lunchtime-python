# Calculate the sum of:
# every odd number from 1 to n
# Where n is a number supplied by the user.
# Submit your answer to the marker bot using functions as shown below. Do not change the name of the functions.

def sum_odd_numbers(n):
    _sum_of_numbers = 0
    for i in range(int(n)):
        if (i % 2 > 0):
            _sum_of_numbers += i
    return _sum_of_numbers

# number = input("Sum of odd numbers from 1 to: ")
# print(sum_odd_numbers(number))
