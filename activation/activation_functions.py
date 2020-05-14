import numpy as np

######## Activation (Forward Propagation) ########

def sigmoid(data):
    return np.sigmoid(data)

def tanh(data):
    return np.tanh(data)

def relu(data):
    return np.maximum(0, data)

def leakyrelu(data, alpha):
    return max(alpha * data, data)

######## Derivative of Activation (Backward Propagation) ########

def sigmoid_diff(data):
    return sigmoid(data) * (1-sigmoid(data))

def tanh_diff(data):
	return 1 - np.power(tanh(data), 2)

def relu_diff(data):
    return 1 if data > 0 else 0

def leakyrelu_diff(data, alpha):
	return 1 if data > 0 else alpha