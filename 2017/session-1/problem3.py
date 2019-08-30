# Build a function that, given a positive integer n, returns a value based on the following:
#
# if n is divisible by 3, return ‘Fizz’
# if n is divisible by 5, return ‘Buzz’
# if n is divisible by 3 and 5, return ‘FizzBuzz’
# if none of the above apply, just return n
# To test your function, iterate over every number from 0 to 100 and print the value returned by your function to the screen.

def fizz_buzz(n):
    # place your code here
    if (n/3 == n//3 and n/5 == n//5):
        return "FizzBuzz"
    elif (n/3 == n//3):
        return "Fizz"
    elif (n/5 == n//5):
        return "Buzz"
    return n

# for i in range(100):
#     print(fizz_buzz(i))
