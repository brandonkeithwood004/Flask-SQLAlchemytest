from flask import Flask

app = Flask(__name__)

def index():
    return "Whats Up"

if__name__== "__main__":
    app.run(debug=True)