from data.models import Clients, CoachExp, Location, State
from data.exts import db
from sqlalchemy.sql import text
from flask import jsonify
import json

def location(gym, town, state):
    findState = State.query.filter_by(state=state).first()
    if findState is None:
        return {"message":"Please enter a valid state"},401
    stateID = findState.stateID
    print(stateID)
    gymtown = Location.query.filter_by(gym=gym, town=town, stateID=stateID).first()
    print("good")
    if gymtown is None:
        new_location=Location(
            gym=gym,
            town=town,
            stateID=stateID
        )
        new_location.save()
        gymtown = Location.query.filter_by(gym=gym, town=town, stateID=stateID).first()
    
    return jsonify({"locationID": gymtown.locationID}), 201


