from Kruskals import Kruskals
import numpy as np
from Graph import Graph

# O(2^n mlogn) running time
def brute(k, graph):
    n = graph.get_nVert()
    options = all_combin(k,n)
    mincost = float('inf')
    for o in options:
        mincost = min(Kruskals(graph,o), mincost)
    return mincost

def all_combin(k,n):
    pointers = [i for i in range(k)]
    options=[]
    loop = True
    while loop:
        options.append([p for p in pointers])
        #update pointers
        if pointers[k-1] < n -1:
            pointers[k-1] +=1
        elif pointers[k-1] == n-1:
            #propogate pointers
            for i in range(1,len(pointers)):
                if pointers[(k-1)-i] < (n-1)-i:
                    pointers[(k-1)-i] +=1
                    if (k-1)-i > 0:
                        pointers[((k-1)-i) + 1] = pointers[(k-1)-i] + 1
                    break
                elif pointers[(k-1)-i] == (n-1)-i and (k-1)-i==0:
                    loop = False
                    break
    return options



            

    
    