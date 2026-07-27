def generate_triangle(n):
    return ["*" * i for i in range(1, n + 1)]
n = int(input("Enter n: "))
for row in generate_triangle(n):
    print(row)