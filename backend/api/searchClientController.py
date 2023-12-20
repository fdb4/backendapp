from app import api2, app
from flask_restx import Resource, fields
from service.searchClientService import searchClient

client_model=api2.model(
    "Clients",
    {
        "email":fields.String(45),
        "firstname":fields.String(45),
        "lastname":fields.String(45)
    }

)

@api2.route('/clients/<int:clientID>')
class ClientSearchResource(Resource):
    @api2.marshal_with(client_model)
    def get(self, clientID):
        """Get a client by id"""
        return searchClient(clientID)
        

