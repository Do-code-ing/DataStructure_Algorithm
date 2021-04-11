# 팩토리얼 구현

n = 5

def factorial(n):
    m = 1
    while n>0:
        m *= n
        n -= 1
    return m

print(factorial(n))
