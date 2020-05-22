import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

from playground.neural_net.layers.dense import Dense
from playground.neural_net.nn_model.forward_propagation import propagate_forward
from playground.neural_net.nn_model.backward_propagation import propagate_backward
import playground.neural_net.optimizers.adam as adam
import playground.neural_net.optimizers.rms_prop as rms_prop
from playground.neural_net.utils.mini_batch import *
import playground.neural_net.optimizers.gd_with_momentum as gd_with_momentum
import playground.neural_net.optimizers.gradient_descent as gradient_descent

from playground.neural_net.loss.cost import compute_cost

class Model:

    def __init__(self):
        self.layers = []
        self.activations = {}
        self.parameters = {}
        self.optimizer = None
        self.learning_rate = 0.0
        self.X = None
        self.y = None
        self.cost = []
        self.v = None
        self.s = None
        self.mini_batch = None

    def init_parameters(self):
        for l in range(1, len(self.layers)):
            if(self.layers[l].activation == 'relu'):
                self.parameters['W' + str(l)] = np.random.randn(self.layers[l].units, self.layers[l-1].units) * np.sqrt(2 / self.layers[l - 1].units)
            else:
                self.parameters['W' + str(l)] = np.random.randn(self.layers[l].units, self.layers[l-1].units) * np.sqrt(1 / self.layers[l - 1].units)
            self.parameters['b' + str(l)] = np.zeros((self.layers[l].units, 1))
            self.activations['Activation' + str(l)] = self.layers[l].activation

    def add(self, units, activation):
        layer = Dense(units, activation)
        self.layers.append(layer)

    def compile(self, opt, lr):
        self.optimizer = opt
        self.init_parameters()

        if(opt == 'Adam'):
            self.v, self.s = adam.initialize_parameters(self.parameters)
        elif(opt == 'GD_momentum'):
            self.v = gd_with_momentum.initialize_parameters(self.parameters)
        elif(opt == 'RMSProp'):
            self.s = rms_prop.initialize_parameters(self.parameters)

        self.learning_rate = lr

    def fit(self, X, Y, epochs, regularization_type, regularization_rate, mini_batch_size):
        self.X = np.array(X).T
        self.Y = np.array(Y).T
        self.mini_batch = create_mini_batches(self.X, self.Y, mini_batch_size)
        costs = []
        t = 0
      
        for i in range(0, epochs):

            for batch in self.mini_batch:
                AL, caches = propagate_forward(batch[0], self.parameters, self.activations)

                cost = compute_cost(AL, batch[1], self.parameters,regularization_type, regularization_rate)
                costs.append(cost)
                
                grads = propagate_backward(AL, batch[1], caches, regularization_type, regularization_rate, self.activations)
                
                if(self.optimizer == 'Adam'):
                    t = t + 1
                    self.parameters, self.v, self.s = adam.update_parameters(self.parameters, grads, self.v, self.s, t, self.learning_rate)
                elif(self.optimizer == 'GD' or self.optimizer == 'Sgd'):
                    self.parameters = gradient_descent.update_parameters(self.parameters, grads, self.learning_rate)
                elif(self.optimizer == 'GD_momentum'):
                    self.parameters, self.v = gd_with_momentum.update_parameters(self.parameters, grads, self.v, 0.9, self.learning_rate)
                elif(self.optimizer=='RMSProp'):
                    self.parameters, self.s = rms_prop.update_parameters(self.parameters, grads, self.s, self.learning_rate)

            if i % 100 == 0:
                print ("Cost after iteration %i: %f" %(i, cost))

        plt.plot(np.squeeze(costs))
        plt.ylabel('cost')
        plt.xlabel('iterations (per tens)')
        plt.title("Learning rate=" + str(self.learning_rate))
        plt.savefig('playground/static/img/test.png')

        
    def predict(self, X, y, type):
        X = np.array(X).T
        y = np.array(y).T
        m = X.shape[1]
        n = len(self.parameters) // 2
        p = np.zeros((1, m))
        
        probas, caches = propagate_forward(X, self.parameters, self.activations)

        if(type == 'classification'):
            for i in range(0, probas.shape[1]):
                print('Predicted: ', probas[0,i])
                if probas[0,i] > 0.5:
                    p[0,i] = 1
                else:
                    p[0,i] = 0
            print("Accuracy: "  + str(np.sum((p == y)/m)))

            return p

        else:
            for i in range(0, probas.shape[1]):
                print(probas[0,i])
        
            return probas