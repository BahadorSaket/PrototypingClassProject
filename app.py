# %load_ext Cython
# %%cython

# import psyco
# psyco.full()




from time import sleep
import os
import copy
import glob
from flask_socketio import SocketIO, send, emit
import pandas as pd
from flask import Flask, render_template, jsonify
from flask import request
from sklearn import svm
import random
import json
import ast
import itertools
import numpy as np
import timeit
from timeit import default_timer as timer



app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template('index.html')


class Transformer(ast.NodeTransformer):
	ALLOWED_NAMES = set(['Decimal', 'None', 'False', 'True'])
	ALLOWED_NODE_TYPES = set([
		'Expression',  # a top node for an expression
		'Tuple',      # makes a tuple
		'Call',       # a function call (hint, Decimal())
		'Name',       # an identifier...
		'Load',       # loads a value of a variable with given identifier
		'Str',        # a string literal
		'Num',        # allow numbers too
		'List',       # and list literals
		'Dict',       # and dicts...
	])

def get_post_MLmodels():
	print "hellow word"


if __name__ == "__main__":    	
    import warnings
    warnings.filterwarnings("ignore")	

    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    #app.run(host = '0.0.0.0', port = port)
    socketio.run(app)
