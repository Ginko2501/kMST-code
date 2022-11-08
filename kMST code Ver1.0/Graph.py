import math
import numpy as np

class Graph(object):
    ''' nVerts: number of vertices
        adj: list of adjacent vertices
        edges: adjacent matrix of the graph '''
    
    def __init__(self, mat):
        mat = np.array(mat, dtype=np.double) # each entry should be doulbe
        self.nVerts = mat.shape[0]
        self.edges = mat
        
        self.adj = [[]] * self.nVerts
        for i in range(self.nVerts):
            for j in range(i):
                if self.edges[i][j] > 0 :
                    self.adj[i] = np.append(self.adj[i], [j])
                    self.adj[j] = np.append(self.adj[j], [i])
        
    def __str__(self):
        return np.array2string(self.edges)
    

    def add_edge(self, i, j, v):
        if self.edges[i][j] == 0:
            self.edges[i][j] = v
            self.edges[j][i] = v
            self.adj[i] = np.append(self.adj[i], [j])
            self.adj[j] = np.append(self.adj[j], [i])
        else:
            self.edges[i][j] = min(self.edges[i][j], v)
            self.edges[j][i] = min(self.edges[j][i], v)

'''
# TEST
G = Graph(np.array([ [0, 2, 1],
                     [2, 0, 3],
                     [1, 3, 0] ]))
G.add_edge(1, 2, 1.5)
print(G)
'''