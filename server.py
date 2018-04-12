#!/usr/bin/python
from flask import Flask, request, render_template

import random, serial

app = Flask(__name__)

@app.route("/")
def index():
        s = serial.Serial('/dev/ttyAMC')
        s.write('p')
        b = s.readline()
        if(b[0]=='1'):
                bgcolor = 'blue'
        else:
                bgcolor = 'green'
        s.close()
        
        render_template('index.html', bgcolor=bgcolor)
        

