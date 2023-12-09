from app import api2, app
from flask_restx import Resource, fields
from flask import request
from service.getMessageService import getMessage
from service.postMessageService import postMessage
message_model=api2.model(
    "message",
    {
        "message":fields.String,
        "SenderFN":fields.String(45),
        "SenderLN": fields.String(45),
        "lastmodified":fields.DateTime, #NOTE 0 by default

    }

)
message_model2=api2.model(
    "message",
    {
        "message":fields.String,
        "clientID":fields.Integer
    }

)

@api2.route('/message/<int:clientID>')
class GenMessageRescource(Resource):
    @api2.marshal_list_with(message_model)
    def get(self, clientID):
        """Get all messages"""
        info = getMessage(clientID)
        return info

    @api2.expect(message_model2)
    def post(self, clientID):
        message=request.json["message"]
        clientID1=request.json["clientID"]
        info= postMessage(clientID1,clientID,message)
        return info

