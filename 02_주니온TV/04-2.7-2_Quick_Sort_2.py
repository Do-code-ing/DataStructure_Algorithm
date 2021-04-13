# 2.7-1
def partition2(S, low, high):
    pivotitem = S[low]
    i = low + 1
    j = high
    while i <= j: # 역전되기 전까지
        while S[i] < pivotitem and i != high: # 오류 수정 (and i != high)
            i += 1
        while S[j] > pivotitem:
            j -= 1
        if i < j:
            S[i], S[j] = S[j], S[i]
        else: # 오류 수정 (else: break)
            break
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    return pivotpoint

# 2.7-2
def quicksort2(S, low, high):
    if high > low:
        pivotpoint = partition2(S, low, high) # pivotpoint = mid
        quicksort2(S, low, pivotpoint-1)
        quicksort2(S, pivotpoint+1, high)

S = [15, 22, 13, 27, 12, 10, 20, 25]
print("Before :", S)
quicksort2(S, 0, len(S)-1)
print(" After :", S)

# S = [26, 5, 37, 1, 61, 11, 59, 15, 48, 19]
# print("Before :", S)
# partition2(S, 0, len(S)-1)
# print(" After :", S)