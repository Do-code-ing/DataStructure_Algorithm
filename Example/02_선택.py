# 선택 (Selection) :
# 입력 : n개의 값과 k(1<= k <= n)값
# 출력 : k번째로 작은 입력 값
# 목표 : 비교 횟수 최소화

# k = n 최대값 찾기
# n-1번의 비교 : 최대값 찾기 가능 : 상한 (Upper Bound)
# n-1번의 비교가 반드시 필요한 경우가 존재한다면, : 하한 (Lower Bound)

# 최대값 찾기 문제

# n-1 ------- U.B : 최대한 상한 이하만큼만 비교하면 된다.
# n-1 ------- L.B : 최소한 하한 이상만큼만 비교하면 된다.

# 상한과 하한이 같기 때문에 완전히 풀린 문제.

# k = 1, n 최대값과, 최소값 찾기
# 순차 비교.
# 최대값 찾기 = n-1
# 최소값 찾기 = n-2
# 즉, 2n-3번 -> UB
# 토너먼트 비교.
# 최대값 찾기 = n-1
# 최소값 찾기 = n/2-1
# 즉, 3n/2-2번 -> LB

# k = 1, 2 최소값과 두번째로 작은 값
# 순차 비교.
# 최소값 찾기 = n-1
# 두번째 작은 값 찾기 = n-2
# 2n-3
# 토너먼트 비교.
# 최소값 찾기 = n-1
# 두번째 작은 값 찾기 = n-log2n-2
# 2n-3 -log2n

# ----------------

# Quick Select 방법

# 1. array에서 array를 둘로 나눌 기준 p를 고른다. (random(p))
# 2. A = [p보다 작은 값]
#    B = [p보다 큰 값]
#    M = [p와 같은 값]
# array = [[A],[M(p)],[B]]
# 3. if len(A) > k:
#       A에서 k번째 작은 값을 찾으면됨 (M과 B에는 없음)
#       재귀적으로 찾으면 됨
#    elif len(A)+len(M) < k:
#       B에서 찾아야함 대신에
#       k = k - len(A) - len(M)인 k번째 작은 값을 찾으면 됨
#    else:
#       return p

def quick_select(L, k):
    p = L[0]
    A, B, M = [], [], []
    for x in L:
        if x < p:
            A.append(x)
        elif x > p:
            B.append(x)
        else:
            M.append(x)
    if len(A) >= k:
        return quick_select(A, k)
    elif len(A)+len(M) < k:
        return quick_select(B, k-len(A)-len(M))
    else:
        return p
L = [6,2,1,3,7,9,10]
print(quick_select(L,3))

# k = 3
# p = 6
# A = [1,2,3]
# M = [6]
# B = [7,9,10]

# Medium of Mediums (MoM) 방법