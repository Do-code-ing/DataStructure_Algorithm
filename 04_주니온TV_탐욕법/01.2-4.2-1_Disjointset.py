class DisjointSet:
    def __init__(self, n):
        self.U = []
        for i in range(n):
            self.U.append(i)

    def find(self, i):
        j = i
        while self.U[j] != j:
            j = self.U[j]
        return j

    def equal(self, p, q):
        if p == q:
            return True
        else:
            return False
    
    def union(self, p, q):
        if p < q:
            self.U[q] = p
        else:
            self.U[p] = q