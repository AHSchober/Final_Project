#!/usr/bin/python
from flask import Flask, request, render_template

import random, serial

app = Flask(__name__)

@app.route("/")
def index():
        s = serial.Serial('/dev/ttyAMC')
        s.write('p')
        if(p):
                bgcolor = 'blue'
        else:
                bgcolor = 'green'
        
        render_template('index.html', bgcolor=val)
        

