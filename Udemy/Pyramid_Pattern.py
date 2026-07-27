def generate_pyramid(n):
    result = []

    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        result.append(spaces + stars + spaces)

    return result