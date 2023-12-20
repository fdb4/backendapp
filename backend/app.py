from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from data.exts import db
from data.models import Clients, GeneralInfo, WorkoutGoal, CoachExp, Location, State, ClientCoaches
from config.config import DevConfig


app=Flask(__name__)
CORS(app)
app.config.from_object(DevConfig)
db.init_app(app)
api2=Api(app,doc='/docs')
def createApp():
    app=Flask(__name__)
    app.app_context().push()
    CORS(app)
    app.config.from_object(DevConfig)
    db.init_app(app)
    api2=Api(app,doc='/docs')
@app.shell_context_processor
def make_shell_context():
    return{
        "db":db,
        "Clients":Clients,
        "GeneralInfo": GeneralInfo,
        "WorkoutGoal": WorkoutGoal,
        "CoachExp": CoachExp,
        "Location": Location,
        "State": State,
        "ClientCoaches": ClientCoaches
    }
    
import api
