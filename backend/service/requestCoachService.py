from data.models import ClientCoaches, Clients
from flask import jsonify

def requestCoach(clientID, coachID):
    out_request = ClientCoaches.query.filter_by(clientID=clientID).first()
    if out_request != None:
        return {"message": "Too many requests"}

    coach = Clients.query.filter_by(clientID=coachID).first()
    coachexpID = coach.coachexpID

    new_request = ClientCoaches(
        clientID=clientID,
        request=None,
        coachexpID=coachexpID
    )

    new_request.save()
    return jsonify({"message": "Request sent successfully"})
