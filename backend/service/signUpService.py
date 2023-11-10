from data.models import Clients
from flask import jsonify, session

def signUpClient(email, password, firstname, lastname):
        
        client=Clients.query.filter_by(email=email).first()

        if client is not None:
            return jsonify({"message":f"User with email {email} already exists"})

        new_client=Clients(
            email=email,
            password=password,
            firstname=firstname,
            lastname=lastname
        )
        new_client.save()
        session["clientID"]=new_client.clientID
        return jsonify({"message": "User created successfuly"})