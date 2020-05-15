import numpy as np

from activation.activation_functions import *

def linear_forward(A, W, b):
    print(W.shape)
    print(A.shape)

    Z = np.dot(W, A.T) + b

    assert Z.shape == (W.shape[0], A.shape[1])
    cache = (A, W, b)

    return Z, cache


def linear_activation_forward(A_prev, W, b, activation):

    if activation == "sigmoid":
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = sigmoid(Z)

    elif activation == "relu":
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = relu(Z)

    elif activation == "tanh":
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = tanh(Z)

    elif activation == "leaky_relu":
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = leakyrelu(Z)

    assert A.shape == (W.shape[0], A_prev.shape[1])
    cache = (linear_cache, activation_cache)

    return A, cache


def L_model_forward(X, parameters):

    caches = []
    A = X
    L = len(parameters)

    for l in range(1, L):
        A_prev = A
        A, cache = linear_activation_forward(
            A_prev,
            parameters["W" + str(l)],
            parameters["b" + str(l)],
            activation="relu",
        )
        caches.append(cache)

    AL, cache = linear_activation_forward(
        A, parameters["W" + str(L)], parameters["b" + str(L)], activation="sigmoid"
    )
    caches.append(cache)

    assert AL.shape == (1, X.shape[1])

    return AL, caches