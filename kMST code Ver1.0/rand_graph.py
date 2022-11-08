import math
import numpy as np

def rand_graph(n, m, bound=100):
    ''' n is the number of vertices
        m is the number of edges
        bound is the upper bound on edge cost '''
    
    g = np.zeros((n,n))
    for k in range(m):
        i = np.random.randint(0, n)
        j = np.random.randint(0, n)
        while i==j or g[i][j]!=0:
            i = np.random.randint(0, n)
            j = np.random.randint(0, n)

        g[i][j] = g[j][i] = np.random.randint(0, bound) + 1
    
    return g
