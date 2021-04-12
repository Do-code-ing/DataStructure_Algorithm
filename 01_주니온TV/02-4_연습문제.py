# 연습문제 1.2.1:
#     - 02-3에서 리스트 f를 사용하지 않아도 되는가?
#     - 만약, 그렇다면 f를 사용하지 않고 반복문으로 피보나치 항을 구하시오.

def fibo2(n):
    x = 0
    y = 1
    for _ in range(2, n+1):
        z = x + y
        x = y
        y = z
    return z

print(fibo2(10))

# 공간 또한 효율적이다.