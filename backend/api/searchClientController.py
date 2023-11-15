from app import api, app
from flask_restx import Resource, fields
from service.searchClientService import searchClient

client_model=api.model(
    "Clients",
    {
        "email":fields.String(45),
        "firstname":fields.String(45),
        "lastname":fields.String(45)
    }

)

@api.route('/clients/<int:clientID>')
class ClientSearchResource(Resource):
    @api.marshal_with(client_model)
    def get(self, clientID):
        """Get a client by id"""
        return searchClient(clientID)
        

