from flask import Flask, request
from models import db

app = Flask(__name__)
db.init_app(app)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/management")
def management():
    return "Management Page"

if __name__ == "__main__":
    app.run()
