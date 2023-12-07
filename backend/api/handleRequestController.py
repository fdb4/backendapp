from app import api2, app
from flask_restx import Resource, fields
from service.handleRequestService import handleRequest
from flask import request

handle_request_model=api2.model(
    "Handle_request",
    {
        "coachID":fields.Integer(),
        "clientID":fields.Integer(),
        "decision":fields.Integer()
    }

)

@api2.route('/coaches/requests')
class handleRequestResource(Resource):
    @api2.expect(handle_request_model)
    def post(self):
        """Accept or decline a client request"""
        coachID=request.json['coachID']
        clientID=request.json['clientID']
        decision=request.json['decision']
        return handleRequest(coachID, clientID, decision)