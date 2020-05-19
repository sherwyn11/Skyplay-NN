from playground.neural_net.nn_model import forward_propagation,backward_propagation
from playground.neural_net.loss import cost

def sgd(X, Y, layers_dims,epochs):

    parameters = initialize_parameters(layers_dims)
    for i in range(0, epochs):
        for j in range(0, m):
            # Forward propagation
            a, caches = forward_propagation.propagate_forward(X[:, j], parameters)
            # Compute cost
            cost += compute_cost(a, Y[:, j])
            # Backward propagation
            grads = backward_propagation.propagate_backward(a, caches, parameters)
            # Update parameters.
            parameters = update_parameters(parameters, grads)
