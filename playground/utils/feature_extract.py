import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder


def get_features(problem_type):
    df = pd.read_csv('playground/clean/clean.csv')
    X = df.iloc[ : , : -1].values
    Y = df.iloc[ : , -1].values

    ### Scaling the X ###

    ss = StandardScaler()
    X = ss.fit_transform(X)

    ### Label Encoding the Y ###
    
    if(problem_type == 'classification'):
        le = LabelEncoder()
        Y = le.fit_transform(Y)

    Y = Y.reshape(-1, 1)

    return X, Y, ss, le

def get_features_for_test(problem_type, ss, le):
    df = pd.read_csv('playground/clean/test.csv')
    X = df.iloc[ : , : -1].values
    Y = df.iloc[ : , -1].values

    ### Scaling the X ###

    X = ss.fit_transform(X)

    ### Label Encoding the Y ###
    
    if(problem_type == 'classification'):
        Y = le.fit_transform(Y)

    Y = Y.reshape(-1, 1)

    return X, Y