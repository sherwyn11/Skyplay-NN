from flask import Flask, request, jsonify, render_template
from playground.neural_net.nn_model.model import Model
from playground import app
import os.path
import numpy as np
import pandas as pd
import secrets
import asyncio
from shutil import copyfile


@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():

    model = Model()
    model.add(2, "sigmoid")
    model.add(4, "sigmoid")
    model.add(1, "sigmoid")
    model.compile("SGD", 0.3)
    model.fit([[0, 0], [0, 1], [1, 0], [1, 1]], [[0], [1], [1], [0]], 5000)
    print(model.predict([[0, 0], [0, 1], [1, 1], [1, 0]], [[0], [1], [0], [1]]))
    print(model.predict([[1, 0], [0, 1], [1, 1], [0, 0]], [[1], [1], [0], [0]]))

    return render_template("preprocess.html", active="home", title="Home",)
