def order(P, i, j):
    if i == j:
        print("A%d"%(i), end="")
    else:
        k = P[i][j]
        print("(", end="")
        order(P, i, k)
        order(P, k+1, j)
        print(")", end="")