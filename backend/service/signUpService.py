from data.models import Clients
from flask import jsonify, session
from werkzeug.security import generate_password_hash

def signUpClient(email, password, firstname, lastname, userType):
        
        client=Clients.query.filter_by(email=email).first()

        if client is not None:
            return jsonify({"message":f"User with email {email} already exists"})

        new_client=Clients(
            email=email,
            password=generate_password_hash(password),
            firstname=firstname,
            lastname=lastname,
            workoutgoalID=None,
            geninfoID=None,
            isCoach=userType,
            coachexpID=None,
            isadmin=None
        )
        new_client.save()
        session["clientID"]=new_client.clientID
        return jsonify({"message": "User created successfully"})