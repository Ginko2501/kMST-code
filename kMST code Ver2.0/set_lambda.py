from globals import *
from primal_dual import *
from prune import *

def set_lambda():
    lambda_l = 0
    lambda_r = INF
    
    while lambda_r - lambda_l > EPS:
        lambda_m = 0.5 * (lambda_l + lambda_r)
        
        idx, comp_list = primal_dual(lambda_m)
        
        num = prune_all(idx, comp_list)
        if num >= K:
            lambda_r = lambda_m
        else:
            lambda_l = lambda_m
        
        print(lambda_m, num)
    
    idx, comp_list = primal_dual(lambda_m)
    print(lambda_m, prune_all(idx, comp_list))
    idx, comp_list = primal_dual(lambda_m + EPS)
    print(lambda_m + EPS, prune_all(idx, comp_list))
    #plot_comp_list(idx, comp_list)

# TEST
set_lambda()