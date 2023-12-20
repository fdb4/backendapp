from app import api, app
from flask_restx import Resource, fields
from service.getActiveRequestService import getActiveRequest
from flask import request

coach_model=api.model(
    "Coaches",
    {
        "clientID":fields.Integer(),
        "email":fields.String(45),
        "firstname":fields.String(45),
        "lastname":fields.String(45),
        "price":fields.Float(),
        "rating":fields.Integer(),
        "experience":fields.Integer(),
        "bio":fields.String(4294967295),
        "gym":fields.String(45),
        "town":fields.String(45),
        "state":fields.String(45),
        "specializations": fields.List(fields.String)
    }

)

@api.route('/client/requests/<int:clientID>')
class getActiveRequestResource(Resource):
    @api.marshal_list_with(coach_model)
    def get(self, clientID):
        """Any pending requests for a client"""

        return getActiveRequest(clientID)