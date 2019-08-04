class UnionFind:
    def __init__(self, n):
        self.N      = N
        self.depth  = [0] * N
        self.parent = list(range(N))

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.depth[x] < self.depth[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.depth[x] == self.depth[y]:
                self.depth[x] += 1

    def are_same(self, x, y):
        return self.find(x) == self.find(y)

    def is_root(self, x):
        return x == self.find(x)

    def num_tree(self):
        return sum([self.is_root(i) for i in range(self.N)])


N, M = map(int, input().split())

T = UnionFind(N)

for m in range(M):
    X, Y, Z  = map(int, input().split())
    T.unite(X-1, Y-1)

print(T.num_tree())
