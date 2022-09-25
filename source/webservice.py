#!/usr/bin/python3
#coding: utf-8

from flask import Flask, make_response, send_file
import random
from glob import iglob

app = Flask(__name__)

@app.route('/random/<path>')
def index(path):
    image = random.choice([i for i in iglob('static/pics/*')])
    return make_response(send_file(image))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')