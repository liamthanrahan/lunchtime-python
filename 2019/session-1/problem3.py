def fizz_buzz(n):
    value = n
    if n % 3 == 0 and n % 5 == 0:
        value = 'FizzBuzz'
    elif n % 3 == 0:
        value = 'Fizz'
    elif n % 5 == 0:
        value = 'Buzz'

    return value

# val = input("Gib me number: ")
# print(fizz_buzz(val))

# for i in range(26):
#     print(fizz_buzz(i))
