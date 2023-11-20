from data.models import Clients
from werkzeug.security import check_password_hash
from flask import jsonify, session
from flask_jwt_session import create_access_token, create_refresh_token


def loginClient(email,password):
        client= Clients.query.filter_by(email=email).first()
        if client is None:
            return {"message":"Wrong email/username"},401
        if not check_password_hash(client.password,password):
            return {"message":"Wrong password"},401
        session["clientID"]=client.clientID
        access_token = create_access_token(identity=client.clientID)
        refresh_token=create_refresh_token(identity=client.clientID)
        return jsonify({"message":"Success", "access_token":access_token, "refresh_token":refresh_token, "coachexpID":client.coachexpID})
