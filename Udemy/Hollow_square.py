# You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings.


def hollow_square(n):
    result = []

    for i in range(n):
        if n == 1:
            result.append('*')
        elif n == 2 or i == 0 or i == n - 1:
            result.append('*' * n)
        else:
            result.append('*' + ' ' * (n - 2) + '*')

    return result


n = int(input('enter n: '))
for row in hollow_square(n):
    print(row)