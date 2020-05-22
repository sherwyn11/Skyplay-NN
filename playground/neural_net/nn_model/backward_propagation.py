from playground.neural_net.activation.activation_functions import *

def linear_backward(dZ, cache, type, lambd):

    A_prev, W, b = cache
    m = A_prev.shape[1]
    if(type == '0'):
        dW = (1/m) * np.dot(dZ, A_prev.T)
    elif(type == 'L1'):
        dW = (1/m) * np.dot(dZ, A_prev.T) + lambd / (2 * m)
    elif(type == 'L2'):
        dW = (1/m) * np.dot(dZ, A_prev.T) + (lambd * W) / m
    db = (1/m) * np.sum(dZ, axis = 1, keepdims = True)
    dA_prev = np.dot(W.T, dZ)
    return dA_prev, dW, db

def linear_activation_backward(dA, cache, activation, regularization_type, regularization_rate,learning_rate):

    linear_cache, activation_cache = cache
    
    if activation == 'relu':
        dZ = relu_backward(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache, regularization_type, regularization_rate)
        
    elif activation == 'sigmoid':
        dZ = sigmoid_backward(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache, regularization_type, regularization_rate)

    elif activation == 'tanh':
        dZ = tanh_backward(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache, regularization_type, regularization_rate)

    elif activation == 'leaky_relu':
        dZ = leakyrelu_backward(dA, learning_rate,activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache, regularization_type, regularization_rate)
    
    return dA_prev, dW, db

def propagate_backward(AL, Y, caches, regularization_type, regularization_rate, activations,learning_rate):

    grads = {}
    L = len(caches) 
    m = AL.shape[1]
    Y = Y.reshape(AL.shape) 

    dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))
    current_cache = caches[L - 1]
    grads['dA' + str(L)], grads['dW' + str(L)], grads['db' + str(L)] = linear_activation_backward(dAL, current_cache, activations['Activation' + str(L)], regularization_type, regularization_rate,learning_rate)
    
    for l in reversed(range(L-1)):
        current_cache = caches[l]
        dA_prev_temp, dW_temp, db_temp = linear_activation_backward(grads['dA' + str(l + 2)], current_cache, activations['Activation' + str(l + 2)], regularization_type, regularization_rate,learning_rate)
        grads['dA' + str(l + 1)] = dA_prev_temp
        grads['dW' + str(l + 1)] = dW_temp
        grads['db' + str(l + 1)] = db_temp

    return grads