import numpy as np

######## (Forward Propagation) ########


def sigmoid(Z):
    A = 1/(1+np.exp(-Z))
    cache = Z
    return A, cache

def relu(Z):    
    A = np.maximum(0,Z)
    assert(A.shape == Z.shape)
    cache = Z 
    return A, cache


def tanh(data):
    return np.tanh(data)

def leakyrelu(data, alpha):
    return max(alpha * data, data)

######## (Backward Propagation) ########

def sigmoid_diff(data):
    return 1/(1+np.exp(-data))

def tanh_diff(data):
    return 1 - np.power(tanh(data), 2)

def relu_diff(data):
    return 1 if data > 0 else 0

def leakyrelu_diff(data, alpha):
    return 1 if data > 0 else alpha


def relu_backward(dA, cache):
    
    Z = cache
    dZ = np.array(dA, copy=True) 

    dZ[Z <= 0] = 0
    assert (dZ.shape == Z.shape)
    return dZ

def sigmoid_backward(dA, cache):
    
    Z = cache
    
    s = 1/(1+np.exp(-Z))
    dZ = dA * s * (1-s)
    
    assert (dZ.shape == Z.shape)
    
    return dZ