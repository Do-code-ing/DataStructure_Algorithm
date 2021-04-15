# 2.9-1: 큰 수 덧셈
def ladd(u, v):
    n = len(u) if len(u) > len(v) else len(v)
    result = []
    carry = 0
    for k in range(n):
        i = u[k] if k < len(u) else 0
        j = v[k] if k < len(v) else 0
        value = i + j + carry
        carry = value // 10
        result.append(value % 10)
    if carry > 0:
        result.append(carry)
    return result

# u = [2, 3, 8, 7, 6, 5]
# v = [3, 2, 7, 3, 2, 4, 9]
# print(567832 + 9423723)
# print(ladd(u,v)[::-1])

# 2.9-2: 큰 수 곱셈(분할정복)
def prod(u, v):
    n = len(u) if len(u) > len(v) else len(v)
    if len(u) == 0 or len(v) == 0: # 곱셈에 0이 있는 경우
        return [0]
    elif n <= threshold:
        return lmult(u, v) # lowlevel multiplication
    else:
        m = n // 2
        x = div(u, m); y = rem(u, m) # div = 몫, rem = 나머지
        w = div(v, m); z = rem(v, m)
        p1 = prod(x, w)
        p2 = ladd(prod(x, z), prod(w, y))
        p3 = prod(y, z)
        return ladd(ladd(exp(p1, 2*m), exp(p2, m)), p3) # exp = 거듭제곱셈

# 2.9-3: 큰 수의 지수 곱셈과 나눗셈
def exp(u, m):
    if u == [0]:
        return [0]
    else:
        return [0] * m + u
    
def div(u, m):
    if len(u) < m:
        u.append(0)
    return u[m:len(u)]

def rem(u, m):
    if len(u) < m:
        u.append(0)
    return u[0:m]

# u = [2, 3, 8, 7, 6, 5]
# print(exp(u, 3))
# print(div(u, 3))
# print(rem(u, 3))

# 2.9-4: 단순 곱셈
def lmult(u, v):
    i = u[0] if 0 < len(u) else 0
    j = v[0] if 0 < len(v) else 0
    value = i * j
    carry = value // 10
    result = []
    result.append(value % 10)
    if carry > 0:
        result.append(carry)
    return result

# print(lmult([8],[7])[::-1])
# print(8*7)

threshold = 1
u = [2, 3, 8, 7, 6, 5]
v = [3, 2, 7, 3, 2, 4, 9]
print(prod(u, v)[::-1])
print(567832*9423723)