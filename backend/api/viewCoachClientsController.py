from app import api2, app
from flask_restx import Resource, fields
from service.viewCoachClientsService import viewCoachClients
from flask import request

view_clients_model=api2.model(
    "View_clients",
    {
        "clientID":fields.Integer(),
        "firstname":fields.String(45),
        "lastname":fields.String(45)
    }

)

@api2.route('/coaches/clients/<int:clientID>')
class viewCoachClientsResource(Resource):
    @api2.marshal_list_with(view_clients_model)
    def get(self, clientID):
        """View all clients for a coach"""
        return viewCoachClients(clientID)
        

