from app import api2, app
from flask_restx import Resource, fields
from flask import request
from service.getConversationsService import getConversations

conversation_model=api2.model(
    "Conversation",
    {
        "clientID":fields.Integer(),
        "firstname":fields.String(45),
        "lastname": fields.String(45),
    }

)

@api2.route('/message/conversations/<int:clientID>')
class GetConversationsRescource(Resource):
    @api2.marshal_list_with(conversation_model)
    def get(self, clientID):
        """Get all conversation previews"""
        info = getConversations(clientID)
        return info

