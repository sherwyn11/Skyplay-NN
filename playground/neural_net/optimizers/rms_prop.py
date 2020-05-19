import numpy as np

def initialize_parameters(parameters) :
    
    L = len(parameters) // 2 
    s = {}
    
    for l in range(L):

        s["dW" + str(l+1)] = np.zeros_like(parameters["W" + str(l + 1)])
        s["db" + str(l+1)] = np.zeros_like(parameters["b" + str(l + 1)])
    
    return s

def update_parameters(parameters, grads, s, learning_rate, beta=0.9, epsilon=1e-8):

    L = len(parameters) // 2                 

    for l in range(L):

        s["dW" + str(l + 1)] = beta * s["dW" + str(l + 1)] + (1 - beta) * np.power(grads['dW' + str(l + 1)], 2)
        s["db" + str(l + 1)] = beta * s["db" + str(l + 1)] + (1 - beta) * np.power(grads['db' + str(l + 1)], 2)

        parameters["W" + str(l + 1)] = parameters["W" + str(l + 1)] - learning_rate * grads["dW" + str(l + 1)] / np.sqrt(s["dW" + str(l + 1)] + epsilon)
        parameters["b" + str(l + 1)] = parameters["b" + str(l + 1)] - learning_rate * grads["db" + str(l + 1)] / np.sqrt(s["db" + str(l + 1)] + epsilon)

    return parameters, s