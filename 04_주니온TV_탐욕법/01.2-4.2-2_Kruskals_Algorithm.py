# 4.2-1
class DisjointSet:
    def __init__(self, n):
        self.U = []
        for i in range(n): # 서로소 집합 만들기
            self.U.append(i)

    def find(self, i): # 대표 집합 찾기
        j = i
        while self.U[j] != j:
            j = self.U[j]
        return j

    def equal(self, p, q): # 사이클 형성 여부
        if p == q:
            return True
        else:
            return False
    
    def union(self, p, q): # 대표한테 몰아주기
        if p < q:
            self.U[q] = p
        else:
            self.U[p] = q

# 4.2-2
def kruskal(n, E):
    F = []
    dset = DisjointSet(n)
    while len(F) < n-1:
        edge = E.pop(0)
        i, j = edge[0], edge[1]
        p = dset.find(i)
        q = dset.find(j)
        if not dset.equal(p, q):
            dset.union(p, q)
            F.append(edge)
    return F

# 가중치 합 구하기
def cost(F):
    total = 0
    for e in F:
        total += e[2]
    return total

n = 5
E = [
    [0, 1, 1],
    [2, 4, 2],
    [0, 2, 3],
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [1, 3, 6]
]

F = kruskal(n, E)
for i in range(len(F)):
    print(F[i])

print(cost(F))