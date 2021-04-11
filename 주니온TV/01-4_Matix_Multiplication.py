def matrixmult(A, B): # 3중 루프
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [[2, 3], [4, 1]]
B = [[5, 7], [6, 8]]
print("A =", A)
# A = [[2, 3], [4, 1]]
print("B =", B)
# B = [[5, 7], [6, 8]]
C = matrixmult(A, B)
print("C =", C)
# C = [[28, 38], [26, 36]]



# A = [[2,3,4],[5,2,1],[1,3,2]]
# B = [[1,3,2],[4,1,3],[1,2,3]]
# print(matrixmult(A,B))