import numpy as np

from layers.dense import Dense
from nn_model.forward_propagation import L_model_forward
from nn_model.backward_propagation import L_model_backward
from nn_model.update_parameters import update_parameters
from nn_model.update_parameters import gradient_check_n
from loss.cost import compute_cost

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
            if(self.layers[l].activation == 'relu'):
                self.parameters['W' + str(l)] = np.random.randn(self.layers[l].units, self.layers[l-1].units) * np.sqrt(2 / self.layers[l - 1].units)
            else:
                self.parameters['W' + str(l)] = np.random.randn(self.layers[l].units, self.layers[l-1].units) * np.sqrt(1 / self.layers[l - 1].units)
            self.parameters['b' + str(l)] = np.zeros((self.layers[l].units, 1))

    def add(self, units, activation):
        layer = Dense(units, activation)
        self.layers.append(layer)

    def compile(self, opt, lr):
        self.optimizer = opt
        self.learning_rate = lr

    def fit(self, X, Y, epochs):
        self.init_parameter()
        self.X = np.array(X).T
        self.Y = np.array(Y).T

        for i in range(0, epochs):
            AL, caches = L_model_forward(self.X, self.parameters)
            cost = compute_cost(AL, self.Y)
            grads = L_model_backward(AL, self.Y, caches)
            parameters = update_parameters(self.parameters, grads, self.learning_rate)
            if i % 10 == 0:
                print ("Cost after iteration %i: %f" %(i, cost))

        gradient_check_n(self.parameters, grads, self.X, self.Y)

        
    def predict(self, X, y):
        X = np.array(X).T
        y = np.array(y).T
        m = X.shape[1]
        n = len(self.parameters) // 2
        p = np.zeros((1,m))
        
        probas, caches = L_model_forward(X, self.parameters)

        for i in range(0, probas.shape[1]):
            print(probas[0,i])
            if probas[0,i] > 0.5:
                p[0,i] = 1
            else:
                p[0,i] = 0
        
        print("Accuracy: "  + str(np.sum((p == y)/m)))
            
        return p


