import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

def get_features(X, Y, problem_type):

    ### Scaling the X ###

    ss = StandardScaler()
    X = ss.fit_transform(X)

    ### Label Encoding the Y ###
    le = LabelEncoder()

    if(problem_type == 'classification'):
        Y = le.fit_transform(Y)

    Y = Y.reshape(-1, 1)

    return X, Y, ss, le

def get_features_for_test(X, Y, problem_type, ss, le):

    ### Scaling the X ###

    X = ss.fit_transform(X)

    ### Label Encoding the Y ###
    
    if(problem_type == 'classification'):
        Y = le.fit_transform(Y)

    Y = Y.reshape(-1, 1)

    return X, Y

def split_data(split_ratio):
    df = pd.read_csv('playground/clean/clean.csv')
    df = df.sample(frac=1).reset_index(drop=True)
    print('Length', len(df))
    if(len(df) > 250):
        df = df.iloc[ : 250, : ]
        df.to_csv('playground/clean/clean.csv', mode='w', index=False)
        df = pd.read_csv('playground/clean/clean.csv')

    X = df.iloc[ : , : -1].values
    Y = df.iloc[ : , -1].values

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=split_ratio/100, random_state=42)

    return X_train, X_test, Y_train, Y_test