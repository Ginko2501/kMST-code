import networkx as nx
import tests

from random import random
from plot_graph import plot_graph

K = 7

ACTIVE = 1
NEUTRAL = 0

EPS = 1.0e-10
INF = 1.0e10

# import from test files
G = tests.greedy1()

# # random graph with n vertices and m edges
# G = nx.gnm_random_graph(10, 15)

# # dense graph with n vertices and m edges
# G = nx.dense_gnm_random_graph

# # sparse graph with n vertices and p probability for each edge
# G = nx.fast_gnp_random_graph

# # dense graph with n vertices and p probability for each edge
# G = nx.gnp_random_graph

# assign node id
for v in G:
    G.nodes[v]['id'] = v

# # random edge weight
# for (u, v) in G.edges:
#     G[u][v]["weight"] = int(9*random()) + 1


# TEST
# plot_graph(G)
#plot_graph(G.subgraph([0,G.adj[0]]))
