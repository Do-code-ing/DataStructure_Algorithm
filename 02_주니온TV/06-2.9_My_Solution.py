# 2.9-1
def dsum(a, b):
    n = len(str(a)) if len(str(a)) > len(str(b)) else len(str(b))
    a = list(int(_) for _ in str(a)[::-1])
    b = list(int(_) for _ in str(b)[::-1])
    while n > len(a):
        a.append(0)
    while n > len(b):
        b.append(0)
    carry = 0
    answer = []
    for k in range(n):
        answer.append((a[k]+b[k]+carry) % 10)
        carry = (a[k]+b[k]+carry) // 10
    if carry > 0:
        answer.append(carry)
    return "".join(str(i) for i in answer[::-1])

a = 567832
b = 9423723
print(567832 + 9423723)
print(dsum(a, b))
