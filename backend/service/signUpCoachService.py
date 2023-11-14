from data.models import CoachExp
from flask import jsonify
from . import locationService, updateClientService
import json

def signUpCoach(clientID, price, experience, bio, gym, town, state):
    location_result = locationService.location(gym, town, state)
    print(1)
    response, status = location_result
    print(2)
    # Check if the status code is 401
    if status == 401:
        print(3)
        return location_result
    print(4)
    # Access the JSON response from the tuple
    location_json = response.json
    locationID = location_json.get("locationID")

    new_coach = CoachExp(
        price=price,
        rating=0.0,
        locationID=locationID,
        experience=experience,
        bio=bio
    )

    new_coach.save()

    coachexpID=new_coach.coachexpID
    updateClientService.updateClient(clientID=clientID, coachexpID=coachexpID)

    return jsonify({"message": "Coach created successfully"})
