def minmult(d):
    n = len(d) - 1
    M = [[-1] * (n+1) for _ in range(n+1)]
    P = [[-1] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        M[i][i] = 0
    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            M[i][j], P[i][j] = minimum(M, d, i, j)
    return M, P

def minimum(M, d, i, j):
    minValue = float("INF")
    mink = 0
    for k in range(i, j):
        value = M[i][k] + M[k+1][j]
        value += d[i-1] * d[k] * d[j]
        if minValue > value:
            minValue = value
            mink = k
    return minValue, mink

d = [5, 2, 3, 4, 6, 7, 8]
print(minmult(d))

# M = 행렬간의 최소 곱셈 횟수
# ([[-1, -1, -1, -1, -1, -1, -1], 
# [-1, 0, 30, 64, 132, 226, 348], 
# [-1, -1, 0, 24, 72, 156, 268], 
# [-1, -1, -1, 0, 72, 198, 366], 
# [-1, -1, -1, -1, 0, 168, 392], 
# [-1, -1, -1, -1, -1, 0, 336], 
# [-1, -1, -1, -1, -1, -1, 0]],
# P = 행렬간의 최소 곱셈 시 어디서 부터 나누어야 하는가
# [[-1, -1, -1, -1, -1, -1, -1], 
# [-1, -1, 1, 1, 1, 1, 1], 
# [-1, -1, -1, 2, 3, 4, 5], 
# [-1, -1, -1, -1, 3, 4, 5], 
# [-1, -1, -1, -1, -1, 4, 5], 
# [-1, -1, -1, -1, -1, -1, 5], 
# [-1, -1, -1, -1, -1, -1, -1]])

# 3.7
def order(P, i, j):
    if i == j:
        print("A%d"%(i), end="")
    else:
        k = P[i][j]
        print("(", end="")
        order(P, i, k)
        order(P, k+1, j)
        print(")", end="")

M, P = minmult(d)
print("M =")
for i in range(1, len(M)):
    print(M[i][1:])
print("P =")
for i in range(1, len(P)):
    print(P[i][1:])

print("minimum order: ", end="")
order(P, 1, len(d)-1)