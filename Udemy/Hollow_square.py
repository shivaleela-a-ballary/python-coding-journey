#You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).
def hollow_square(n):
    result=[]
    for i in range(n):
        if i==0 or i==n-1:
            result.append('*'*n)
        else:
            if n=1:
                result.append(*)
            else:
                result.append('*'+''*(n-2)+'*')
    return result