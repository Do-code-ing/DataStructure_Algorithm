def floyd2(W):
    n = len(W)
    D = W
    P = [[-1] * n for _ in range(n)] # i에서 j로 갈 때 어느 정점 k를 지나쳐 갈 것인가
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k # 지나쳐 갈 때 정점 저장
    return D, P

INF = 999
W = [
    [0, 1, INF, 1 ,5],
    [9, 0, 3, 2, INF],
    [INF, INF, 0, 4, INF],
    [INF, INF, 2, 0 ,3],
    [3, INF, INF, INF, 0]
]

D, P = floyd2(W)
for i in range(len(D)):
    print(D[i])
print()
for i in range(len(P)):
    print(P[i])