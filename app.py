# !/usr/bin/env python3
# coding: utf-8

from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return "Welcome!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port = '5000')
