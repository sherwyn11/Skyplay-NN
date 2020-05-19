def sgd(X, Y, layers_dims):

    X = data_input
    Y = labels
    parameters = initialize_parameters(layers_dims)
    for i in range(0, num_iterations):
        for j in range(0, m):
            # Forward propagation
            a, caches = forward_propagation(X[:, j], parameters)
            # Compute cost
            cost += compute_cost(a, Y[:, j])
            # Backward propagation
            grads = backward_propagation(a, caches, parameters)
            # Update parameters.
            parameters = update_parameters(parameters, grads)
