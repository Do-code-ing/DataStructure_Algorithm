# 피보나치 수열의 n 번째 항 구하기
#     - 피보나치 수열: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#     - 피보나치 수열의 (재귀적)정의
#         - f0 = 0, f1 = 1
#         - fn = fn-1 + fn-2, (n>=2)
def fibo(n):
    f = [0,1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

for i in range(2000):
    print(fibo(i), end=" ")