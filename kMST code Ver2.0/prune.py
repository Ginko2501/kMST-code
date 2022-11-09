from globals import *
import component
from primal_dual import *

def prune_comp(G, idx, comp_list):
    # pruning step
    res = nx.Graph.copy(G)
    
    flag = True
    while flag:
        # pruning might result in new prunable components
        flag = False
        for comp in comp_list:
            if comp.state == NEUTRAL and len(component.cut(comp, res)) == 1:
                flag = True
                # prune comp in G
                for v in comp:
                    if res.has_node(v):
                        res.remove_node(v)
    
    return res
    
def prune_all(idx, comp_list):
    res = 0
    
    for i in range(len(comp_list)):
        comp = comp_list[i]
        if i != idx[list(comp.nodes)[0]]:
            continue
        
        pruned = prune_comp(comp, idx, comp_list)
        if len(list(pruned.nodes)) > res:
            res = len(list(pruned.nodes))
    
    return res
    
            