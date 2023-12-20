from app import api, app
from flask_restx import Resource, fields
from service.fireCoachService import fireCoach
from flask import request

request_model=api.model(
    "Request",
    {
        "clientID":fields.Integer(),
        "coachID":fields.Integer()
        
    }

)

@api.route('/client/fireCoach')
class fireCoachRescource(Resource):
    @api.expect(request_model)
    def post(self):
        """Fire a coach"""
        clientID=request.json['clientID']
        coachID=request.json['coachID']
        return fireCoach(clientID, coachID)