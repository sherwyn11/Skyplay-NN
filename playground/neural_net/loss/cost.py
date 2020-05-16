import numpy as np

def compute_cost(AL, Y):
    m = Y.shape[1]

    cost = -np.sum(np.multiply(Y,np.log(AL))+np.multiply(1-Y,np.log(1-AL)))/m
    
    cost = np.squeeze(cost)
    assert(cost.shape == ())
    
    return cost