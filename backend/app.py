from flask import Flask
from flask_restx import Api
from data.exts import db
from config.config import DevConfig

app=Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)
api=Api(app,doc='/docs')

@app.shell_context_processor
def make_shell_context():
    return{
        "db":db,
        "Clients":Clients
    }

import api