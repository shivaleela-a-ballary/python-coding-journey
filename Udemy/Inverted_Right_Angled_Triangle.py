def generate_inverted_triangle(n):
    return["*"* i for i in range(n,0,-1)]
n=int(input('enter n:'))
for row in generate_inverted_triangle(n):
    print(row)