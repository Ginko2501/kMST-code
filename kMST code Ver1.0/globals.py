import math
from Graph import Graph
from rand_graph import rand_graph

EPS = 1e-5; # the smallest number for consideration
NEUTRAL = 0
ACTIVE = 1
LAMBDA = 2

# keep graph G as a global instance
G = Graph(rand_graph(3, 2, 5)) 
print(G)
