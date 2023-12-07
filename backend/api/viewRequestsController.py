from app import api2, app
from flask_restx import Resource, fields
from service.viewRequestsService import viewRequests
from flask import request

view_request_model=api2.model(
    "View_request",
    {
        "clientID":fields.Integer(),
        "firstname":fields.String(45),
        "lastname":fields.String(45)
    }

)

@api2.route('/coaches/requests/<int:clientID>')
class ViewRequestsResource(Resource):
    @api2.marshal_list_with(view_request_model)
    def get(self, clientID):
        """View requests for a coach"""
        return viewRequests(clientID)
        

