class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    def find_set(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]


    def union(self, x, y):
        root_x = self.find_set(x)
        root_y = self.find_set(y)
    
        if root_x == root_y:
            return
    
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

