def partition(S, low, high):
    pivotitem = S[low]
    j = low
    for i in range(low+1, high+1):
        if S[i] < pivotitem:
            j += 1
            S[i], S[j] = S[j], S[i]
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    return pivotpoint