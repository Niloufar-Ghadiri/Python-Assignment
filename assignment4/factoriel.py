def Factorial(n):
    total = 1
    i=1
    while total<=n:
        total*=i
        i+=1
        if total==n:
            return True
    return False
number = int(input())
if Factorial(number):
    print('Yes')
else:
    print('No')