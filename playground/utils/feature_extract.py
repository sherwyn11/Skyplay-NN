import numpy as np
import pandas as pd

def get_features():
    df = pd.read_csv('playground/clean/clean.csv')
    X = df.iloc[ : , : -1]
    Y = df.iloc[ : , -1]
    X = X.values
    Y = Y.values.reshape(-1, 1)
    
    return X, Y