import networkx as nx
import matplotlib.pyplot as plt

def plot_graph(G):
    # get node positions
    # set seed for reproducibility
    pos = nx.spring_layout(G, seed=1)

    # draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=150)

    # draw edges
    nx.draw_networkx_edges(G, pos, width=2)

    # draw edge labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    
    # node labels
    node_labels = nx.get_node_attributes(G, "id")
    nx.draw_networkx_labels(G, pos, node_labels)
    
    plt.show()