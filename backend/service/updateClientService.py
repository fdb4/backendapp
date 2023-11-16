from data.models import Clients
from flask import jsonify
from werkzeug.security import generate_password_hash

def updateClient(clientID=None, email=None, password=None, firstname=None, lastname=None, workoutGoalID=None, geninfoID=None, coachexpID=None):
    print("Client ID")
    print(clientID)
    client=Clients.query.filter_by(clientID=clientID).first() 

    if email is None:
        email=client.email
    if password is None:
        password=client.password
    else:
        password=generate_password_hash(password)
    if firstname is None:
        firstname=client.firstname
    if lastname is None:
        lastname=client.lastname
    if workoutGoalID is None:
        workoutGoalID=client.workoutgoalID
    if geninfoID is None:
        geninfoID=client.geninfoID
    if coachexpID is None:
        coachexpID=client.coachexpID
    print("COACHEXPID:")
    print(coachexpID)
    client.update(email, password, firstname, lastname, workoutGoalID, geninfoID, coachexpID)
    return jsonify({"message": "Client successfully updated"})

    