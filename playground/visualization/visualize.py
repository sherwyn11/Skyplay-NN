import pandas as pd
import matplotlib
import asyncio
import time
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import os
import csv


def get_columns():
    df = pd.read_csv("playground/clean/clean.csv")
    return df.columns

def pair_plot():
    df = pd.read_csv("playground/clean/clean.csv")
    start=time.time()
    sns_plot = sns.pairplot(df, height=2.5)
    mid=time.time()
    sns_plot.savefig("playground/static/img/pairplot.png")
    end=time.time()
    print(f'{mid-start} {end-mid} {sns_plot}')
    return True


def xy_plot(col1, col2):
    df = pd.read_csv("playground/clean/clean.csv")
    return df

def hist_plot(df,feature_x):
    x= df[feature_x]
    x.to_csv("playground/visualization/col.csv",mode="w", index=False,header=['price'])
    with open("playground/visualization/col.csv", 'r') as filehandle:
        lines = filehandle.readlines()
        lines[-1]=lines[-1].strip()
    with open("playground/visualization/col.csv", 'w') as csvfile:
        for i in lines:
            csvfile.write(i)  
    return True
