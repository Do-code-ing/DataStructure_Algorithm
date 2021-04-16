def partition2(S, low, high):
    pivotitem = S[low]
    i = low + 1
    j = high
    while i <= j: # 역전되기 전까지
        while S[i] < pivotitem:
            i += 1
        while S[j] > pivotitem:
            j -= 1
        if i < j:
            S[i], S[j] = S[j], S[i]
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    return pivotpoint