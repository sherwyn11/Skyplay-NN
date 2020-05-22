import numpy as np

######## (Forward Propagation) ########

def sigmoid(Z):
    A = 1/(1+np.exp(-Z))
    cache = Z
    return A, cache

def tanh(data):
    cache=data
    value=np.tanh(data)
    return value, cache


def relu(Z):
    A = np.maximum(0, Z)
    cache = Z 
    return A, cache


def leakyrelu(data,alpha):
    cache=data
    A=np.maximum(alpha * data, data)
    return A,cache

######## (Backward Propagation) ########

def sigmoid_backward(dA, cache):
    
    Z = cache
    s = 1/(1+np.exp(-Z))
    dZ = dA * s * (1-s)
    
    assert (dZ.shape == Z.shape)
    return dZ

def tanh_backward(dA, cache):
    
    Z = cache
    
    dZ =  1 - np.power(np.tanh(dA), 2)
    assert (dZ.shape == Z.shape)
    return dZ

def relu_backward(dA, cache):
    
    Z = cache
    dZ = np.array(dA, copy=True) 
    dZ[Z <= 0] = 0
    
    assert (dZ.shape == Z.shape)
    return dZ

def leakyrelu_backward(dA, alpha,cache):
    Z = cache
    dZ= np.where( dA > 0, 1, alpha)
    assert (dZ.shape == Z.shape)
    return dZ