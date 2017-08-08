def is_prime(n):
    if (int(n) < 2):
        return False
    for i in range(2, int(n)):
        if (int(n) % i == 0):
            return False
    return True

# print(is_prime(input("is prime: ")))
