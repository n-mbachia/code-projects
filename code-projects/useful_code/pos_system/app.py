#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'This is the project that you must finish Mbachia!'

if __name__ == '__main__':
    app.run(debug=True)
