'''
Created on Jan 31, 2016

@author: sikarwar
'''
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()