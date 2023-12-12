from app import api, app
from flask_restx import Resource, fields
from flask import request
from service.getMessageService import getMessage
from service.postMessageService import postMessage
message_model=api.model(
    "message",
    {
        "message":fields.String,
        "SenderFN":fields.String(45),
        "SenderLN": fields.String(45),
        "lastmodified":fields.DateTime, #NOTE 0 by default

    }

)
message_model2=api.model(
    "message2",
    {
        "message":fields.String,
        "clientID":fields.Integer

    }

)


@api.route('/message/<int:clientID>')
class GenMessageRescource(Resource):
    @api.marshal_list_with(message_model)
    @api.expect(message_model2)
    def get(self, clientID):
        """Get all messages"""
        clientID1 = request.json["clientID"]
        info = getMessage(clientID1,clientID))
        return info
    @api.expect(message_model2)
    def post(self, clientID):
        message=request.json["message"]
        clientID1=request.json["clientID"]
        info= postMessage(clientID1,clientID,message)
        return info

