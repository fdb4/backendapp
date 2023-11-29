from app import api, app
from flask_restx import Resource, fields
from service.requestCoachService import requestCoach
from flask import request

request_model=api.model(
    "Request",
    {
        "clientID":fields.Integer(),
        "coachID":fields.Integer()
        
    }

)

@api.route('/client/sendRequest')
class RequestCoachRescource(Resource):
    @api.expect(request_model)
    def post(self):
        """Request a coach as a client"""
        clientID=request.json['clientID']
        coachID=request.json['coachID']
        return requestCoach(clientID, coachID)