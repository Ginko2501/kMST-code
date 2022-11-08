import Graph

class UnionFind:
    def __init__(self, n):
        self.components = [i for i in range(n)]
        self.backing = [{i} for i in range(n)]

    def Find(self, u):
        return self.components[u]
    
    def Union(self, a, b):
        A = self.backing[a]
        B = self.backing[b]

        if len(A) > len(B):
            for v in B:
                self.backing[a].add(v)
                self.components[v] = a
        else:
            for v in A:
                self.backing[b].add(v)
                self.components[v] = b

# O(mlogn) excpeted runtime
# implementation of kruskals algorithm
def Kruskals(graph, vert_on):
    edges = graph.get_edges()

    on_edges = []

    k = len(vert_on)

    for e in edges:
        if e[1]in vert_on and e[2] in vert_on:
            on_edges.append(e)

    on_edges.sort(key = lambda edge : edge[0])

    u = UnionFind(vert_on)

    #O(n)
    i = 0
    cost = 0
    while i < k:
        v= on_edges[i][1]
        w = on_edges[i][2]

        if u.Find(v) != u.Find(w):
            cost += on_edges[i][0]
            u.Union(u.Find(v), u.Find(w))
        i+=1

    return cost



