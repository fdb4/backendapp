from app import api2, app
from flask_restx import Resource, fields
from service.unsendRequestService import unsendRequest
from flask import request

request_model=api2.model(
    "Request",
    {
        "clientID":fields.Integer(),
        "coachID":fields.Integer()
        
    }

)

@api2.route('/client/unsendRequest')
class UnrequestCoachRescource(Resource):
    @api2.expect(request_model)
    def post(self):
        """Unsend a request as a client"""
        clientID=request.json['clientID']
        coachID=request.json['coachID']
        return unsendRequest(clientID, coachID)
