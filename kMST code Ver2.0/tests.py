import networkx as nx

# 2 vertices and 1 edge
def hello_world():
    # initialize empty graph
    G = nx.Graph()
    
    # nodes
    G.add_node(0)
    G.add_node(1)
    
    # edges
    G.add_edge(0, 1, weight = 30.0)
    
    return G

# a simple triangle
def triangle():
    G = nx.Graph()
    
    G.add_node(0)
    G.add_node(1)
    G.add_node(2)
    
    G.add_edge(0, 1, weight=1)
    G.add_edge(0, 2, weight=1)
    G.add_edge(1, 2, weight=2)
    
    return G

# 5 vertices, 5 edges
def small1():
    G = nx.Graph()
    
    G.add_node(0)
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)
    
    G.add_edge(0, 1, weight=1.0)
    G.add_edge(0, 2, weight=3.0)
    G.add_edge(0, 3, weight=2.0)
    G.add_edge(1, 4, weight=1.0)
    G.add_edge(2, 3, weight=3.0)
    
    return G

# 5 vertices, 5 edges
def small2():
    G = nx.Graph()
    
    G.add_node(0)
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)
    
    
    G.add_edge(0, 2, weight=2.0)
    G.add_edge(0, 4, weight=1.0)
    G.add_edge(1, 2, weight=3.0)
    G.add_edge(1, 4, weight=1.0)
    G.add_edge(2, 3, weight=2.0)
    
    return G

# 10 vertices, 10 edges
# when lambda=2, there is a tie break whether the 
# last comp goes neutral or the last eddge goes tight
def middle1():
    G = nx.Graph()
    for i in range(10):
        G.add_node(i)
    G.add_edge(0,6,weight=2)
    G.add_edge(0,4,weight=4)
    G.add_edge(1,2,weight=7)
    G.add_edge(2,3,weight=4)
    G.add_edge(2,8,weight=6)
    G.add_edge(2,9,weight=9.5)
    G.add_edge(3,4,weight=1)
    G.add_edge(4,5,weight=1)
    G.add_edge(4,7,weight=1)
    return G

def prune1():
    G = nx.Graph()
    