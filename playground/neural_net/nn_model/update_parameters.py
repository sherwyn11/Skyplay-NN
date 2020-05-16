import numpy as np

def update_parameters(parameters, grads, learning_rate):
  
    L = len(parameters) // 2

    for l in range(L):
        parameters["W" + str(l+1)] = parameters["W" + str(l+1)]  - learning_rate * grads["dW" + str(l+1)]
        parameters["b" + str(l+1)] = parameters["b" + str(l+1)] - learning_rate * grads["db" + str(l+1)] 
   
    return parameters


# def dictionary_to_vector(parameters):
#     """
#     Roll all our parameters dictionary into a single vector satisfying our specific required shape.
#     """
#     keys = []
#     count = 0
#     for key in parameters:
        
#         # flatten parameter
#         new_vector = np.reshape(parameters[key], (-1,1))
#         keys = keys + [key]*new_vector.shape[0]
        
#         if count == 0:
#             theta = new_vector
#         else:
#             theta = np.concatenate((theta, new_vector), axis=0)
#         count = count + 1

#     return theta, keys

# def vector_to_dictionary(theta):
#     """
#     Unroll all our parameters dictionary from a single vector satisfying our specific required shape.
#     """
#     parameters = {}
#     parameters["W1"] = theta[:8].reshape((4,2))
#     parameters["b1"] = theta[8:12].reshape((4,1))
#     parameters["W2"] = theta[12:16].reshape((1,4))
#     parameters["b2"] = theta[16:17].reshape((1,1))

#     return parameters

# def gradients_to_vector(gradients):
#     """
#     Roll all our gradients dictionary into a single vector satisfying our specific required shape.
#     """
    
#     count = 0
#     for key in gradients:
#         # flatten parameter
#         new_vector = np.reshape(gradients[key], (-1,1))
        
#         if count == 0:
#             theta = new_vector
#         else:
#             theta = np.concatenate((theta, new_vector), axis=0)
#         count = count + 1

#     return theta

# def gradient_check_n(parameters, gradients, X, Y, epsilon = 1e-7):

#     parameters_values, _ = dictionary_to_vector(parameters)
#     grad = gradients_to_vector(gradients)
#     num_parameters = parameters_values.shape[0]
#     J_plus = np.zeros((num_parameters, 1))
#     J_minus = np.zeros((num_parameters, 1))
#     gradapprox = np.zeros((num_parameters, 1))
    
#     for i in range(num_parameters):

#         thetaplus =  np.copy(parameters_values)                                       
#         thetaplus[i][0] = thetaplus[i][0] + epsilon                                   
#         J_plus[i], _ =  forward_propagation_n(X, Y, vector_to_dictionary(thetaplus))  

#         thetaminus = np.copy(parameters_values)                                       
#         thetaminus[i][0] = thetaminus[i][0] - epsilon                                         
#         J_minus[i], _ = forward_propagation_n(X, Y, vector_to_dictionary(thetaminus)) 

#         gradapprox[i] = (J_plus[i] - J_minus[i]) / (2 * epsilon)

#     numerator = np.linalg.norm(grad - gradapprox)                                     
#     denominator = np.linalg.norm(grad) + np.linalg.norm(gradapprox)                   
#     difference = numerator / denominator                                              

#     if difference > 2e-7:
#         print ("\033[93m" + "There is a mistake in the backward propagation! difference = " + str(difference) + "\033[0m")
#     else:
#         print ("\033[92m" + "Your backward propagation works perfectly fine! difference = " + str(difference) + "\033[0m")
    
#     return difference