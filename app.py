from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')