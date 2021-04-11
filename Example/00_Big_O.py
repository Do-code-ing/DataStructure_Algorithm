def increment_one(a):
    return a+1

# T(n) = 1
# 최고차항은 n**0
# 즉 T(n) = O(1)

def number_of_bits(n):
    count = 0
    while n > 0:
        n = n//2
        count +=1
    return count

# T(n) = O(log2n)

# y = a**x
# logay = x