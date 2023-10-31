from flask import Flask,jsonify
from flask_restx import Api,Resource

from config.dbcon import dbcon
app=Flask(__name__)
api=Api(app,doc='/docs')

db=dbcon()


@app.route('/')
def test():
    return "hi"
if __name__ == '__main__':
    app.run()