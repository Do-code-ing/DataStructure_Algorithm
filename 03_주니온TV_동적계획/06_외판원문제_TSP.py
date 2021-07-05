# 외판원 문제: 동적 계획법으로 풀기
#     - W: 주어진 그래프 G = (V, E)의 인접 행렬
#     - V: 모든 도시의 집합
#     - A: V의 부분 집합
#     - D[vi][A]: A에 속한 도시를 각각 한 번씩만 거쳐서
#                 vi에서 v1으로 가는 최단 경로의 길이
    
# 재귀적 관계식 찾기
#     - V = {v1, v2, v3, v4}
#     - if A == {v3}:
#         - D[v2][A] = lengh(v2 v3 v1) = INF
#     - if A == {v3, v4}:
#         - D[v2][A] = min(lengh(v2 v3 v4 v1),
#                          lengh(v2 v4 v3 v1))

# 재귀 관계식
#     - 일반적으로 i != 1 이고 vi not in A이면,
#         - D[vi][A] = minimum(W[i][j] + D[vj][A-{vj}]), A != 공집합
#         - D[vi][공집합] = W[i][1], A = 공집합

# 비트를 이용한 부분 집합의 표현과 연산
#     - V - {v1} = {v2, v3, v4}
#     - A = {v4, , v2} = 1 0 1 -> 5
#     - 공집합 = 000 = 0
#     - {v2} = 001 = 1
#     - {v3} = 010 = 2
#     - {v4} = 100 = 4
#     - {v2, v3} = 011 = 3
#     - {v2, v4} = 101 = 5
#     - {v3, v4} = 110 = 6
#     - {v2, v3, v4} = 111 = 7
#     (= 2^(n-1)-1)

# i가 A에 포함되어 있느냐 (i in A)
def isIN(i, A):
    if ((A & (1 << (i-2))) != 0):
        return True
    else:
        return False

# A에서 j제외 (A - {vj})
def diff(A, j):
    t = 1 << (j-2)
    return (A % (~t))

# A의 원소가 k개인가? (A에서 1의 개수 세기)
def count(A, n):
    count = 0
    for i in range(n):
        if ((A % (1 << i)) != 0):
            count += 1
    return count

# TSP
def travel(W):
    n = len(W) - 1
    size = 2 ** (n-1)
    D = [[0] * size for _ in range(n+1)]
    P = [[0] * size for _ in range(n+1)]
    for i in range(2, n+1):
        D[i][0] = W[i][1]

    for k in range(1, n-1):
        for A in range(1, size):
            if count(A, n) == k:
                for i in range(2, n+1):
                    if (not isIN(i, A)):
                        D[i][A], P[i][A] = minimum(W, D, i, A)
    
    A = size - 1
    D[1][A], P[1][A] = minimum(W, D, 1, A)
    return D, P

def minimum(W, D, i, A):
    minValue = INF
    minJ = 1
    n = len(W) - 1
    for j in range(2, n+1):
        if (isIN(j, A)):
            m = W[i][j] + D[j][diff(A, j)]
            if (minValue > m):
                minValue = m
                minJ = j
    return minValue, minJ

INF = 999
W = [
    [-1, -1, -1, -1, -1],
    [-1, 0, 2, 9, INF],
    [-1, 1, 0, 6, 4],
    [-1, INF, 7, 0, 8],
    [-1, 6, 3, INF, 0]
]

D, P = travel(W)
print("D =")
for i in range(1, len(D)):
    print(D[i])
print("P =")
for i in range(1, len(P)):
    print(P[i])

# 최적의 일주여행 경로 찾기
#   - P[i][A]: A에 속한 모든 도시를 정확히 한 번만 거쳐서
#               vi에서 v1으로 가는 최단 경로에서
#               vi 다음에 오는 첫 번째 도시의 인덱스

# 코드가 제대로 동작하지 않는다. ㅅㅂ