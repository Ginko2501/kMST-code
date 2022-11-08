import networkx as nx

def test1():
    G = nx.Graph()
    
    G.add_node(0)
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)
    
    for v in G:
        G.nodes[v]['id'] = v
    
    G.add_edge(0, 1, weight=1.0)
    G.add_edge(0, 2, weight=3.0)
    G.add_edge(0, 3, weight=2.0)
    G.add_edge(1, 4, weight=1.0)
    G.add_edge(2, 3, weight=3.0)
    
    return G
    