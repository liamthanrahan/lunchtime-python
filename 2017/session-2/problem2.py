def build_triangle(n):
    triangle = ""
    for i in range(int(n)):
        triangle += "*" * (i + 1)
        if (i != int(n) - 1):
            triangle += "\n"
    return triangle

print(build_triangle(5))
