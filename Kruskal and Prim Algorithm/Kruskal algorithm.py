
class Disjointset:
    def __init__(self, n):
        self.U = []
        for i in range(n):
            self.U.append(i)

    def equal(self, p, q):
        if p == q:
            return True
        else:
            return False

    def find(self, i):
        j = i
        while self.U[j] != j:
            j = self.U[j]

        return j

    def union(self, p, q):
        if p < q:
            self.U[q] = p
        else:
            self.U[p] = q


def kruskal(n, E):
    F = []
    dset = Disjointset(n)
    while len(f) < n - 1:
        edge = E.pop(0)
        i, j = edge[0], edge[1]
        p = dset.find(i)
        q = dste.find(j)
        if not dset.equal(p, q):
            dset.union(p, q)
            F.append(edge)
    return F