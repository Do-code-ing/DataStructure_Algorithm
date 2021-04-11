# recursion

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

for i in range(11):
    print(fib(i), end=" ")

# 시간 복잡도가 안좋다.