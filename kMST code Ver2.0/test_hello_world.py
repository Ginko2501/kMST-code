import networkx as nx

def hello_world():
    # initialize empty graph
    G = nx.Graph()
    
    # nodes
    G.add_node(0)
    G.add_node(1)
    
    # edges
    G.add_edge(0, 1, weight = 30.0)
    
    return G
    
