def sum_multiples(n):
    total = 0
    for i in range(int(n)):
        if (is_multiple(i)):
            total += i
    return total

def is_multiple(i):
    return (i % 3 == 0 or i % 5 == 0)

print(sum_multiples(10))
