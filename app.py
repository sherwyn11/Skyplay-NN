from flask import Flask, request, jsonify, render_template
from nn_model.model import Model


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    model = Model()
    model.add(2, "sigmoid")
    model.add(4, "sigmoid")
    model.add(1, "sigmoid")
    model.compile("SGD", 0.3)
    model.fit([[0, 0], [0, 1], [1, 0], [1, 1]], [[0], [1], [1], [0]], 5000)
    print(model.predict([[0, 0], [0, 1], [1, 1], [1, 0]], [[0], [1], [0], [1]]))
    print(model.predict([[1, 0], [0, 1], [1, 1], [0, 0]], [[1], [1], [0], [0]]))

    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0")
