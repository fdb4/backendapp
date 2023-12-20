from app import api, app
from flask_restx import Resource, fields
from service.unsendRequestService import unsendRequest
from flask import request

request_model=api.model(
    "Request",
    {
        "clientID":fields.Integer(),
        "coachID":fields.Integer()
        
    }

)

@api.route('/client/unsendRequest')
class UnrequestCoachRescource(Resource):
    @api.expect(request_model)
    def post(self):
        """Unsend a request as a client"""
        clientID=request.json['clientID']
        coachID=request.json['coachID']
        return unsendRequest(clientID, coachID)