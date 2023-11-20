from app import api
from flask_restx import Resource, fields
from service.searchClientService import searchClient
from flask_jwt_extended import jwt_required

client_model=api.model(
    "Clients",
    {
        "email":fields.String(45),
        "password":fields.String(45),
        "firstname":fields.String(45),
        "lastname":fields.String(45)
    }

)

@api.route('/clients/<int:clientID>')
class ClientSearchResource(Resource):
    @api.marshal_with(client_model)
    @jwt_required()
    def get(self, clientID):
        """Get a client by id"""
        return searchClient(clientID)