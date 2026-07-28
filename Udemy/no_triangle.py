#Right Angled Triangle with Numbers Problem Description: You are given an integer n. Your task is to return a right-angled triangle pattern where each row contains repeated digits. The first row contains the number 1 repeated once, the second row contains the number 2 repeated twice, and so on until the nth row contains the number n repeated n times.
def no_triangle(n):
    pattern=[]
    for i in range(1,n+1):
        pattern.append(str(i)*i)
    return pattern
n=int(input('Enter the no. of rows:'))
print(no_triangle(n))
