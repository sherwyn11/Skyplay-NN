def create_mini_batches(X, Y, mini_batch_size = 64, seed = 0):

    np.random.seed(seed)            
    m = X.shape[1]                
    mini_batches = []
        
    permutation = list(np.random.permutation(m))
    shuffled_X = X[:, permutation]
    shuffled_Y = Y[:, permutation].reshape((1,m))

    num_complete_minibatches = math.floor(m/mini_batch_size) 
    for k in range(0, num_complete_minibatches):

        mini_batch_X = shuffled_X[ : ,k * mini_batch_size : (k + 1) * mini_batch_size]
        mini_batch_Y = shuffled_Y[ : ,k * mini_batch_size : (k + 1) * mini_batch_size]

        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)
    
    if m % mini_batch_size != 0:

        mini_batch_X = shuffled_X[ : ,num_complete_minibatches * mini_batch_size: ]
        mini_batch_Y = shuffled_Y[ : ,num_complete_minibatches * mini_batch_size: ]

        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)
    
    return mini_batches