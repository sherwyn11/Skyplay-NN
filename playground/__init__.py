from flask import Flask, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "5791628bb0b13ce0c676dfde280ba245"
app.secret_key = "Sherwu&DNaz"

from playground import routes
