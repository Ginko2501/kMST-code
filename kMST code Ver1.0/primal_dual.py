import math
import numpy as np
from globals import *
from Graph import Graph
from Component import Component
from Component_List  import Component_List

def primal_dual():
    neutral = Component_List()
    active = Component_List()
    for v in range(G.nVerts):
        active.append(Component(v))
    
    while active.size() != 0:
        residual = G.edges
        
        for comp in active:
            comp.potential -= EPS
            for e in comp.cut:
                residual[e[0]][e[1]] -= EPS
                
                # edge event
                if residual[e[0]][e[1]] == 0:
                    for c in active:
                        if c.contain(e[1]):
                            active.append(Component.merge(comp, c))
                            active.remove(c)
                            active.remove(comp)
            
            # set event
            if comp.potential == 0:
                comp.state = NEUTRAL
                neutral.append(comp)
                active.remove(comp)
        
