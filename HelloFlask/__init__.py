# -*- coding : utf-8 -*-
import sys
# sys.getdefaultencoding('utf8')
from flask import Flask


app = Flask(__name__)

@app.route('/main')
def init():
    return "Hello My HomePage"
