# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
def primeChecker(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
for i in range(a):
    num = int(input())
    if primeChecker(num):
        print('Prime')
    else:
        print('Not prime')