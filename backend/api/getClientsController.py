from app import api, app
from flask_restx import Resource, fields
from service.getClientsService import getClients

client_model=api.model(
    "Clients",
    {
        "email":fields.String(45),
        "firstname":fields.String(45),
        "lastname":fields.String(45)
    }

)

@api.route('/clients')
class ClientsResource(Resource):
    @api.marshal_list_with(client_model)
    def get(self):
        """Get all Clients"""
        clients = getClients()
        return clients