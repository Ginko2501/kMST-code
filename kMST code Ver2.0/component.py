import networkx as nx
import matplotlib.pyplot as plt

from globals import *

def init(v):
    # initialize component with a vertex
    comp = nx.Graph.copy(G.subgraph([v]))
    comp.state = ACTIVE
    comp.potential = LAMBDA
    return comp

def merge(u, v, comp_u, comp_v):
    # merge two components
    comp = nx.compose(comp_u, comp_v)
    #comp = nx.disjoint_union(comp_u, comp_v)
    comp.add_edge(u, v, weight=G[u][v]['weight'])
    # comp = G.subgraph(list(comp1.nodes) + list(comp2.nodes))
    comp.state = ACTIVE
    comp.potential = comp_u.potential + comp_v.potential
    return comp

def find(v, comp_list):
    # find which component in comp_list contains vertex v
    for comp in comp_list:
        if comp.has_node(v):
            return comp

def cut(comp):
    # compute the cut of comp in G
    edges = []
    for (u,v) in G.edges:
        if comp.has_node(u) != comp.has_node(v):
            edges += [(u,v)]
    return edges

def print_comp(comp):
    # print component
    print("state: ", comp.state)
    print("potential: ", comp.potential)
    print("adj list: ", comp.adj)

# # TEST init
# components = [None] * 10
# for n in G:
#     components[n] = init(n)

# # TEST merge
# for n in G:
#     components[0] = merge(components[0], components[n])

# print(components[0].adj)

# # TEST cut
# components = [init(v) for v in G]
# components[0] = merge(components[0], components[1])

# print(G.adj)
# print(cut(components[0]))
