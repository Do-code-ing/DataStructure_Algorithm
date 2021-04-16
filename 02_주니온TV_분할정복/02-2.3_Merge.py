def merge(U, V):
    S = []
    i = j = 0
    while i < len(U) and j < len(V):
        if U[i] < V[j]:
            S.append(U[i])
            i += 1
        else:
            S.append(V[j])
            j += 1
    if i < len(U):
        S += U[i:len(U)]
    else:
        S += V[j:len(V)]
    return S