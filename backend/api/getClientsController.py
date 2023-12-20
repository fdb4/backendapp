from app import api2, app
from flask_restx import Resource, fields
from service.getClientsService import getClients

client_model=api2.model(
    "Clients",
    {
        "email":fields.String(45),
        "firstname":fields.String(45),
        "lastname":fields.String(45)
    }

)

@api2.route('/clients')
class ClientsResource(Resource):
    @api2.marshal_list_with(client_model)
    def get(self):
        """Get all Clients"""
        clients = getClients()
        return clients