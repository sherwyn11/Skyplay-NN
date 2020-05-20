import numpy as np

######## (Forward Propagation) ########

def sigmoid(Z):
    A = 1/(1+np.exp(-Z))
    cache = Z
    return A, cache

def tanh(data):
    return np.tanh(data), data


def relu(Z):
    A = np.maximum(0, Z)
    cache = Z 
    return A, cache


def leakyrelu(data, alpha):
    return max(alpha * data, data)

######## (Backward Propagation) ########

def sigmoid_backward(dA, cache):
    
    Z = cache
    s = 1/(1+np.exp(-Z))
    dZ = dA * s * (1-s)
    
    assert (dZ.shape == Z.shape)
    return dZ

def tanh_backward(dA, cache):
    
    Z = cache

    dZ =  1 - np.power(tanh(dA), 2)
    assert (dZ.shape == Z.shape)
    return dZ

def relu_backward(dA, cache):
    
    Z = cache
    dZ = np.array(dA, copy=True) 
    dZ[Z <= 0] = 0
    assert (dZ.shape == Z.shape)
    return dZ

# TO-DO: Leaky relu back
def leakyrelu_diff(data, alpha):
    Z = cache

    return 1 if data > 0 else alpha