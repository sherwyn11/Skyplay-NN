from flask import session, flash
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder


def read_dataset(filepath):
    if session['ext'] == 'csv':
        df = pd.read_csv(filepath)
    elif session['ext'] == 'json':
        df = pd.read_json(filepath)
    elif session['ext'] == 'xlsx':
        df = pd.read_excel(filepath)
    else:
        flash(f'Error! Matching extension not found', 'danger')
    return df


def get_columns(df):
    return df.columns


def delete_column(df, column_name):
    df = df.drop(column_name, axis=1)
    return df


def get_description(df):
    return df.describe()


def get_head(df):
    return df.head()


def get_dim(df):
    return (df.shape[0], df.shape[1])

def drop_allsame(df):
    to_drop = list()
    for i in df.columns:
        if len(df.loc[:, i].unique()) == 1:
            to_drop.append(i)
    return df.drop(to_drop, axis=1)


def treat_missing_numeric(df, columns, how='mean'):
    if how == 'mean':
        for i in columns:
            print('Filling missing values with mean for columns - {0}'.format(i))
            df.ix[:, i] = df.ix[:, i].fillna(df.ix[:, i].mean())

    elif how == 'mode':
        for i in columns:
            print('Filling missing values with mode for columns - {0}'.format(i))
            df.ix[:, i] = df.ix[:, i].fillna(df.ix[:, i].mode())

    elif how == 'median':
        for i in columns:
            print('Filling missing values with median for columns - {0}'.format(i))
            df.ix[:, i] = df.ix[:, i].fillna(df.ix[:, i].median())

    elif how == 'ffill':
        for i in columns:
            print(
                'Filling missing values with forward fill for columns - {0}'.format(i)
            )
            df.ix[:, i] = df.ix[:, i].fillna(method='ffill')

    elif type(how) == int or type(how) == float:
        for i in columns:
            print('Filling missing values with {0} for columns - {1}'.format(how, i))
            df.ix[:, i] = df.ix[:, i].fillna(how)
    else:
        print('Missing value fill cannot be completed')
    return df


def treat_missing_categorical(df, columns, how='mode'):

    if how == 'mode':
        for i in columns:
            print('Filling missing values with mode for columns - {0}'.format(i))
            df.ix[:, i] = df.ix[:, i].fillna(df.ix[:, i].mode()[0])
    elif type(how) == str:
        for i in columns:
            print('Filling missing values with {0} for columns - {1}'.format(how, i))
            df.ix[:, i] = df.ix[:, i].fillna(how)
    elif type(how) == int or type(how) == float:
        for i in columns:
            print('Filling missing values with {0} for columns - {1}'.format(how, i))
            df.ix[:, i] = df.ix[:, i].fillna(str(how))
    else:
        print('Missing value fill cannot be completed')
    return df


def arrange_columns(target):
    df = read_dataset('playground/clean/clean.csv')
    cols = df.columns.tolist()
    ind = cols.index(target)
    cols[ind], cols[-1] = cols[-1], cols[ind]
    df = df[cols]
    df.to_csv('playground/clean/clean.csv', mode='w', index=False)