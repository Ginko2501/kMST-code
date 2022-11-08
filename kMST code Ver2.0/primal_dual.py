from globals import *
import component

global idx
global comp_list

def print_comp_list():
    for i in range(len(comp_list)):
        comp = comp_list[i]
        if i != idx[list(comp.nodes)[0]]:
            continue
        component.print_comp(comp)
        print()

def primal_dual():
    # idx[v] maintains the index of thecomponent that v is in
    global idx
    idx = [None] * len(G) 
    
    # the list of all components
    global comp_list
    comp_list = []

    # initialize
    for v in G:
        idx[v] = v
        comp_list += [component.init(v)]
    
    # TEST init
    # for i in range(len(comp_list)):
    #     print(idx[i], comp_list[i].adj)
    # return
    
    # residual graph maintain leftover edges and their costs
    residual = nx.Graph.copy(G)
    
    num_active = len(G)
    while num_active != 0:
        # TEST component list
        print_comp_list()
        
        # compute next set event
        t_next_set = INF
        next_sets = [] # stores index of the components
        for i in range(len(comp_list)):
            comp = comp_list[i]
            
            # skip already neutral componenets
            if comp.potential == 0:
                continue
            
            # skip merged components
            if i != idx[list(comp.nodes)[0]]:
                continue
            
            # compare with the current next set event
            if comp.potential < t_next_set:
                t_next_set = comp.potential
                next_sets = [i]
            elif comp.potential == t_next_set:
                # WARNING: potential numerical issues
                next_sets += [i]
        
        # TEST next sets
        print("t_next_set: ", t_next_set)
        print("next_sets: ", next_sets)
                
        # compute next edge event
        t_next_edge = INF
        next_edges = []
        for (u,v) in residual.edges:
            # compute the components that u,v are in
            comp_u = comp_list[idx[u]]
            comp_v = comp_list[idx[v]]
            # comp_u = component.find(u, comp_list)
            # comp_v = component.find(v, comp_list)
            
            if comp_u == comp_v:
                # if two vertices of an edge are in the same component, 
                # remove this edge from the residual graph
                residual.remove_edge(u, v)
                continue
            
            # compute time for this edge to go tight
            if comp_u.state==NEUTRAL and comp_v.state==NEUTRAL:
                continue
            elif comp_u.state==ACTIVE and comp_v.state==ACTIVE:
                t = residual[u][v]['weight'] / 2.0
            else:
                t = residual[u][v]['weight']
            
            # compare with the current next edge event
            if t < t_next_edge:
                t_next_edge = t
                next_edges = [(u,v)]
            elif t == t_next_edge:
                next_edges += [(u,v)]
    
        # TEST next edges
        print("t_next_Edge: ", t_next_edge)
        print("next_edges: ", next_edges)
    
        # set event
        if t_next_set < t_next_edge:
            # TEST enter set event
            print("enter set event")
            
            # update order matters here            
            # update residual graph
            for (u,v) in residual.edges:
                comp_u = comp_list[idx[u]]
                comp_v = comp_list[idx[v]]
                if comp_u.state==ACTIVE and comp_v.state==ACTIVE:
                    residual[u][v]['weight'] -= 2 * t_next_set
                else:
                    residual[u][v]['weight'] -= t_next_set
            
            # update component potential
            for i in range(len(comp_list)):
                comp = comp_list[i]
                if comp.potential == 0:
                    continue
                if i != idx[list(comp.nodes)[0]]:
                    continue
                
                if comp.state == ACTIVE:
                    comp.potential -= t_next_set
            
            # update next sets to NEUTRAL
            for i in next_sets:
                comp = comp_list[i]
                comp.state = NEUTRAL
                num_active = num_active - 1
                 
        #edge event
        elif t_next_set > t_next_edge:
            # TEST enter edge event
            print("enter edge event")
            
            # update order matters here            
            # update residual graph
            for (u,v) in residual.edges:
                comp_u = comp_list[idx[u]]
                comp_v = comp_list[idx[v]]
                if comp_u.state==ACTIVE and comp_v.state==ACTIVE:
                    residual[u][v]['weight'] -= 2 * t_next_edge
                else:
                    residual[u][v]['weight'] -= t_next_edge
                
                # remove next edges from the residual graph
                if residual[u][v]['weight'] == 0:
                    residual.remove_edge(u, v)
            
            # update component potential
            for i in range(len(comp_list)):
                comp = comp_list[i]
                if comp.potential == 0:
                    continue
                if i != idx[list(comp.nodes)[0]]:
                    continue
                
                if comp.state == ACTIVE:
                    comp.potential -= t_next_edge
            
            # update components adjacent to next edges
            for (u,v) in next_edges:
                comp_u = comp_list[idx[u]]
                comp_v = comp_list[idx[v]]
                # comp_u = component.find(u, comp_list)
                # comp_v = component.find(v, comp_list)
                
                # TEST comp_u, comp_v
                # print(comp_u.adj)
                # print(comp_v.adj)

                if comp_u == comp_v:
                    # WARNING: does not break tie when two edges connect the same two components
                    continue
                
                # # purely for the convience of iterating through comp_list
                # comp_u.potential = 0
                # comp_v.potential = 0
                
                # compute the new merged component
                comp_new = component.merge(u, v, comp_u, comp_v)
                comp_list += [comp_new]
                
                # # TEST compe_new
                # print(comp_new.adj)
                
                # update vertex indices
                idx_new = len(comp_list) - 1
                for v in comp_new:
                    idx[v] = idx_new
                
                # update number of current active component
                num_active += 1 - comp_u.state - comp_v.state
                
        
        # tie break!
        else:
            # TEST enter tie break
            print("enter tie break")
            return

    print_comp_list()
        

# TEST
plot_graph(G)

primal_dual()

H = nx.Graph()
for i in range(len(comp_list)):
    comp = comp_list[i]
    if i != idx[list(comp.nodes)[0]]:
        continue
    
    H = nx.disjoint_union(H, comp_list[i])
plot_graph(H)