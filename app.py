from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "testHello, this is a sample Python Web App running on Flask Framework!"

