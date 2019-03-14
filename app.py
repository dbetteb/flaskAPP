# !/usr/bin/env python3
# coding: utf-8

from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

# definition de la racine
@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port = '5000')
