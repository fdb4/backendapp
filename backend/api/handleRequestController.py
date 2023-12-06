from app import api, app
from flask_restx import Resource, fields
from service.handleRequestService import handleRequest
from flask import request

handle_request_model=api.model(
    "Handle_request",
    {
        "coachID":fields.Integer(),
        "clientID":fields.Integer(),
        "decision":fields.Integer()
    }

)

@api.route('/coaches/requests')
class handleRequestResource(Resource):
    @api.expect(handle_request_model)
    def post(self):
        """Accept or decline a client request"""
        coachID=request.json['coachID']
        clientID=request.json['clientID']
        decision=request.json['decision']
        return handleRequest(coachID, clientID, decision)