import math
import numpy as np
from globals import *

class Component(object):
    ''' vertices is the list of vertices in the component
        potential is the potential '''
    
    def __init__(self):
        # initiate empty component
        self.state = ACTIVE
        self.potential = 0
        self.vertices = np.array([])
        self.edges = np.array([])
        self.cut = np.array([])
    
    def init(v):
        # initiate with one vertex
        comp = Component()
        comp.state = ACTIVE
        comp.potential = LAMBDA
        comp.vertices = np.array([v])
        comp.edges = np.array([])
        comp.cut = [[v, w] for w in G.adj[v]]
        return comp
    
    def __str__(self):
        return np.array2string(self.vertices)
    
    def contain(self, v):
        return np.argwhere(self.vertices==v).size != 0
    
    def merge(e, comp1, comp2):
        comp = Component()
        comp.state = ACTIVE
        comp.potential = comp1.potential + comp2.potential
        comp.vertices = np.append(comp1.vertices, comp2.vertices)
        comp.edges = np.append(comp1.edges, comp1.edges)
        comp.edges = np.append(comp.edges, e)
        
        comp.cut = np.array([])
        for e in comp1.cut:
            if not comp2.contain(e[1]):
                comp.cut = np.append(comp.cut, e)
        for e in comp2.cut:
            if not comp1.contain(e[0]):
                comp.cut = np.append(comp.cut, e)
        
        comp.sub_comp1 = comp1
        comp.sub_comp2 = comp2

        

# TEST
c1 = Component.init(1)
c2 = Component.init(2)

print(G.adj[0])

print(c1)
print(c2)
print(c1.contain(1))
print(c1.contain(0))

c = Component.merge([1,2], c1, c2)
print(c)
    
    