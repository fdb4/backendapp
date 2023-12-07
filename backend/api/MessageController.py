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

@api2.route('/message/<int:clientID>')
class GenMessageRescource(Resource):
    @api2.marshal_list_with(message_model)
    def get(self, clientID):
        """Get all messages"""
        info = getMessage(clientID)
        return info
    def post(self, clientID):
        message=request.json["message"]
        info= postMessage(clientID,message)
        return info

