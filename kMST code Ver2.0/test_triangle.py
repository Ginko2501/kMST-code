import networkx as nx

def triangle():
    G = nx.Graph()
    
    G.add_node(0)
    G.add_node(1)
    G.add_node(2)
    
    G.add_edge(0, 1, weight=1)
    G.add_edge(0, 2, weight=1)
    G.add_edge(1, 2, weight=2)
    
    return G