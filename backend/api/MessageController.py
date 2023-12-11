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
    def get(self, clientID):
        """Get all messages"""
        info = getMessage(clientID)
        return info
    @api.expect(message_model2)
    def post(self, clientIDR):
        message=request.json["message"]
        clientIDS=request.json["clientID"]
        info= postMessage(clientIDS,clientIDR,message)
        return info

