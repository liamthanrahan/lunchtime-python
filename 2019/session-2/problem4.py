def is_prime(n):
    if (n == 0 or n == 1):
        return False
    n_is_prime_number = True
    for index in range(2, n):
        if n % index == 0:
            n_is_prime_number = False
            break
    return n_is_prime_number


# print(is_prime(12))
