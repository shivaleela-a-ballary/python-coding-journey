def floyd_triangle(n):
    pattern = []
    num = 1

    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append(str(num))
            num += 1
        pattern.append(" ".join(row))

    return pattern