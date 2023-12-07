from data.models import Clients
from werkzeug.security import check_password_hash
from flask import jsonify, session


def loginClient(email,password):
        client= Clients.query.filter_by(email=email).first()
        if client is None:
            return {"message":"Wrong email/username"},401
        if not check_password_hash(client.password,password):
            return {"message":"Wrong password"},401
        session["clientID"]=client.clientID
        session["isadmin"]=client.isadmin
        return jsonify({"message":"Success", "clientID":client.clientID,"coachexpID":client.isCoach,"adminID":client.isadmin})
