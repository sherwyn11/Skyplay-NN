import numpy as np

def initialize_parameters(parameters):
    
    L = len(parameters) // 2 
    v = {}
    
    for l in range(L):
        v["dW" + str(l+1)] = np.zeros(((parameters['W' + str(l + 1)]).shape))
        v["db" + str(l+1)] = np.zeros(((parameters['b' + str(l + 1)]).shape))
        
    return v

def update_parameters(parameters, grads, v, beta, learning_rate):

    L = len(parameters) // 2 
    
    for l in range(L):

        v["dW" + str(l+1)] = (beta * v['dW' + str(l + 1)]) + ((1 - beta) * grads['dW' + str(l + 1)])
        v["db" + str(l+1)] = (beta * v['db' + str(l + 1)]) + ((1 - beta) * grads['db' + str(l + 1)])

        parameters["W" + str(l+1)] = parameters["W" + str(l+1)] - learning_rate * v["dW" + str(l+1)]
        parameters["b" + str(l+1)] = parameters["b" + str(l+1)] - learning_rate * v["db" + str(l+1)]
        
    return parameters, v