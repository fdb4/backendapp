from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from data.exts import db
from data.models import Clients, GeneralInfo, WorkoutGoal, CoachExp, Location, State, ClientCoaches
from config.config import DevConfig
from flask_jwt_sxtended import JWTManager

app=Flask(__name__)
CORS(app)
app.config.from_object(DevConfig)
db.init_app(app)
JWTManager(app)
api=Api(app,doc='/docs')

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
