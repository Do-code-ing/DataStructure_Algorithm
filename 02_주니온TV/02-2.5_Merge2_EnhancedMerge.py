def merge2(S, low, mid, high):
    U = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if S[i] < S[j]:
            U.append(S[i])
            i += 1
        else:
            U.append(S[j])
            j += 1
    if i <= mid:
        U += S[i:mid+1]
    else:
        U += S[j:high+1]
    for k in range(low, high+1):
        S[k] = U[k-low]