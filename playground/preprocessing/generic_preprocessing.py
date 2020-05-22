from flask import session, flash
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder


def read_dataset(filepath):

    if session["ext"] == "csv":
        df = pd.read_csv(filepath)
    elif session["ext"] == "json":
        df = pd.read_json(filepath)
    elif session["ext"] == "xlsx":
        df = pd.read_excel(filepath)
    else:
        flash(f"Error! Matching extension not found", "danger")
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
    """
    Function to print the dimensions of a given python dataframe
    Required Input -
        - df = Pandas DataFrame
    Expected Output -
        - Data size
    """
    return (df.shape[0], df.shape[1])


def missing_value_analysis(df):
    """
    Function to do basic missing value analysis
    Required Input - 
        - df = Pandas DataFrame
    Expected Output -
        - Chart of Missing value co-occurance
        - Chart of Missing value heatmap
    """
    # msno.matrix(df)

    # msno.heatmap(df)


def drop_allsame(df):
    """
    Function to remove any columns which have same value all across
    Required Input - 
        - df = Pandas DataFrame
    Expected Output -
        - Pandas dataframe with dropped no variation columns
    """
    to_drop = list()
    for i in df.columns:
        if len(df.loc[:, i].unique()) == 1:
            to_drop.append(i)
    return df.drop(to_drop, axis=1)


def treat_missing_numeric(df, columns, how="mean"):
    """
    Function to treat missing values in numeric columns
    Required Input - 
        - df = Pandas DataFrame
        - columns = List input of all the columns need to be imputed
        - how = valid values are 'mean', 'mode', 'median','ffill', numeric value
    Expected Output -
        - Pandas dataframe with imputed missing value in mentioned columns
    """
    if how == "mean":
        for i in columns:
            print("Filling missing values with mean for columns - {0}".format(i))
            df.ix[:, i] = df.ix[:, i].fillna(df.ix[:, i].mean())

    elif how == "mode":
        for i in columns:
            print("Filling missing values with mode for columns - {0}".format(i))
            df.ix[:, i] = df.ix[:, i].fillna(df.ix[:, i].mode())

    elif how == "median":
        for i in columns:
            print("Filling missing values with median for columns - {0}".format(i))
            df.ix[:, i] = df.ix[:, i].fillna(df.ix[:, i].median())

    elif how == "ffill":
        for i in columns:
            print(
                "Filling missing values with forward fill for columns - {0}".format(i)
            )
            df.ix[:, i] = df.ix[:, i].fillna(method="ffill")

    elif type(how) == int or type(how) == float:
        for i in columns:
            print("Filling missing values with {0} for columns - {1}".format(how, i))
            df.ix[:, i] = df.ix[:, i].fillna(how)
    else:
        print("Missing value fill cannot be completed")
    return df


def treat_missing_categorical(df, columns, how="mode"):
    """
    Function to treat missing values in numeric columns
    Required Input - 
        - df = Pandas DataFrame
        - columns = List input of all the columns need to be imputed
        - how = valid values are 'mode', any string or numeric value
    Expected Output -
        - Pandas dataframe with imputed missing value in mentioned columns
    """
    if how == "mode":
        for i in columns:
            print("Filling missing values with mode for columns - {0}".format(i))
            df.ix[:, i] = df.ix[:, i].fillna(df.ix[:, i].mode()[0])
    elif type(how) == str:
        for i in columns:
            print("Filling missing values with {0} for columns - {1}".format(how, i))
            df.ix[:, i] = df.ix[:, i].fillna(how)
    elif type(how) == int or type(how) == float:
        for i in columns:
            print("Filling missing values with {0} for columns - {1}".format(how, i))
            df.ix[:, i] = df.ix[:, i].fillna(str(how))
    else:
        print("Missing value fill cannot be completed")
    return df

    def z_scaler(df, columns):
        """
    Function to standardize features by removing the mean and scaling to unit variance
    Required Input - 
        - df = Pandas DataFrame
        - columns = List input of all the columns which needs to be min-max scaled
    Expected Output -
        - df = Python DataFrame with Min-Max scaled attributes
        - scaler = Function which contains the scaling rules
    """

    scaler = StandardScaler()
    data = pd.DataFrame(scaler.fit_transform(df.loc[:, columns]))
    data.index = df.index
    data.columns = columns
    return data, scaler


def label_encoder(df, columns):
    """
    Function to label encode
    Required Input - 
        - df = Pandas DataFrame
        - columns = List input of all the columns which needs to be label encoded
    Expected Output -
        - df = Pandas DataFrame with lable encoded columns
        - le_dict = Dictionary of all the column and their label encoders
    """
    le_dict = {}
    for c in columns:
        print("Label encoding column - {0}".format(c))
        lbl = LabelEncoder()
        lbl.fit(list(df[c].values.astype("str")))
        df[c] = lbl.transform(list(df[c].values.astype("str")))
        le_dict[c] = lbl
    return df, le_dict


def arrange_columns(target):
    df = read_dataset("playground/clean/clean.csv")
    cols = df.columns.tolist()
    ind = cols.index(target)
    cols[ind], cols[-1] = cols[-1], cols[ind]
    df = df[cols]
    df.to_csv("playground/clean/clean.csv", mode="w", index=False)
