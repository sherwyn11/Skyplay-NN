import numpy as np

from layers.dense import Dense
from nn_model.forward_propagation import L_model_forward
from nn_model.backward_propagation import L_model_backward
from nn_model.update_parameters import update_parameters

class Model:

    def __init__(self):
        self.layers = []
        self.parameters = {}
        self.optimizer = None
        self.learning_rate = 0.0
        self.X = None
        self.y = None
        self.cost = []

    def init_parameter(self):
        for l in range(1, len(self.layers)):
            self.parameters['W' + str(l)] = np.random.randn(self.layers[l].units, self.layers[l-1].units) * 0.01
            self.parameters['b' + str(l)] = np.zeros((self.layers[l].units, 1))

    def add(self, units, activation):
        layer = Dense(units, activation)
        self.layers.append(layer)

    def compile(self, opt, lr):
        self.optimizer = opt
        self.learning_rate = lr

    def fit(self, X, Y, epochs):
        self.init_parameter()
        print(self.parameters)
        self.X = np.array(X)
        self.Y = np.array(Y)

        for i in range(0, epochs):
            AL, caches = L_model_forward(self.X, self.parameters)
            self.cost[i] = compute_cost(AL, self.Y)
            grads = L_model_backward(AL, self.Y, caches)
            parameters = update_parameters(self.parameters, grads, self.learning_rate)