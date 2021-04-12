# iterative

def fib2(n):
    f = [0] * (n+1) # 리스트 컴프리핸션, 배열 초기화
    if n > 0:
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
    return f[n]

for i in range(11):
    print(fib2(i), end=" ")

# 시간 효율은 좋으나, 공간 효율은 02-2보다 안좋다.