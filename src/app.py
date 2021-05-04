from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Essa é a versão 1.0"