import math
import numpy as np
from globals import *

def set_lambda(G):
    lambda_l = 0
    lambda_r = np.inf

    while lambda_r - lambda_l >= EPS:
        LAMBDA = 0.5 * (lambda_l + lambda_r)

        # primal_dual(G)
        
        # prune(G)
    

# TEST
print(LAMBDA)
    