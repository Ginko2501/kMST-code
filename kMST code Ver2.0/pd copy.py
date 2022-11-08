from unionfind import unionfind
from globals import *

# ASSUMPTIONS: n nodes means vertices are 0...n-1
# there is only one edge between nodes (if multiple, keep cheapest)

def primal_dual(lambda1):

    ## Start PD
    y_S = [0 for _ in range(n)]
    pi_S = [lambda1 for _ in range(n)]
    # edges across cut of S
    delta_S = [[] for _ in range(n)]
    active_S = [True for _ in range(n)]

    U = unionfind(n)

    # edges
    unselected_edges = []
    for e in G.edges:
        u,v =e
        delta_S[U.find(u)].append(e)
        delta_S[U.find(v)].append(e)
        unselected_edges.append(e)
    
    pd = []

    num_active = n 
    while num_active > 0:

        # Calculate distance until next set event and which set goes neutral
        next_set_event = float('inf')
        next_set = -1
        for i in range(n):
            s = U.find(i)
            if pi_S[s] < next_set_event:
                next_set_event = pi_S[s]
                next_set = s


        # Calculate distance until next edge event and which edge goes tight
        next_edge_event = float('inf')
        next_edge = (-1,-1)
        for e in unselected_edges:
            u,v = e

            sum_of_ys = []
            for i in range(n):
                for ed in delta_S[U.find(i)]:
                    if ed == e and y_S[U.find(i)] not in sum_of_ys:
                        sum_of_ys.append(y_S[U.find(i)])
            val = G[u][v]["weight"] - (sum(sum_of_ys) / (active_S[U.find(u)] + active_S[U.find(v)]))

            if val < next_edge_event:
                next_edge_event = val
                next_edge = e


        # SET EVENT
        if next_set_event < next_edge_event:
            active_S[next_set] = False
            num_active -=1

        # EDGE EVENT
        else:
            unselected_edges.remove(e)
            pd.append(e)

            # update sets
            set1 = U.find(next_edge[0])
            set2 = U.find(next_edge[1])

            if set1 != set2:
                if (active_S[set1] and active_S[set2]):
                    num_active -=1
                U.unite(set1,set2)

                # check merge
                assert U.find(next_edge[1]) == U.find(next_edge[0])

                pi_S[U.find(next_edge[1])] = pi_S[set1] + pi_S[set2]
                delta_S[U.find(next_edge[1])] = delta_S[set1] + delta_S[set2]
                delta_S[U.find(next_edge[1])] = [i for i in delta_S[U.find(next_edge[1])] if i != e]


        # update y_S
        for e in unselected_edges:
            u,v = e
            set_u = U.find(u)
            set_v = U.find(v)

            if active_S[set_u] and active_S[set_v]:
                y_S[set_u] += .5
                y_S[set_v] += .5
            elif active_S(set_u):
                y_S[set_u] += 1
            elif active_S(v):
                y_S[set_v] += 1
    return pd

print(primal_dual(2))