#!/usr/bin/python
from flask import Flask, request, render_template

import random, serial

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World!"
        s = serial.Serial('/dev/ttyAMC')
        s.write('p')
        

