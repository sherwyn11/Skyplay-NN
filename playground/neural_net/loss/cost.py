import numpy as np

def compute_cost(AL, Y, parameters, type, lambd):
    m = Y.shape[1]
    
    #### Cross - Entropy cost ####

    logprobs = np.multiply(-np.log(AL), Y) + np.multiply(-np.log(1 - AL), 1 - Y)
    cost = 1./m * np.nansum(logprobs)
    
    cost = np.squeeze(cost)

    if(type == '0'):
        return cost
        
    #### Regularization cost ####

    else:
        len_parameters = len(parameters) // 2

        if(type == 'L1'):
            for l in range(len_parameters):
                W = parameters['W' + str(l + 1)]
                if(l == 0):
                    sqr_sum = np.sum(W)
                else:
                    sqr_sum = sqr_sum + np.sum(W)

            L1_regularization_cost = lambd * (sqr_sum) / (2 * m)
            cost = cost + L1_regularization_cost

        elif(type == 'L2'):
            for l in range(len_parameters):
                W = parameters['W' + str(l + 1)]
                if(l == 0):
                    sqr_sum = np.sum(np.square(W))
                else:
                    sqr_sum = sqr_sum + np.sum(np.square(W))

            L2_regularization_cost = lambd * (sqr_sum) / (2 * m)
            cost = cost + L2_regularization_cost

        return cost