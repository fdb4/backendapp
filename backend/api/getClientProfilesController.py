from app import api2, app
from flask_restx import Resource, fields
from service.getClientProfilesService import getClientProfiles

genInfo_model=api2.model(
    "genInfo",
    {
        "firstname":fields.String(45),
        "lastname":fields.String(45),
        "email":fields.String(45),
        "height":fields.Float(),
        "weight":fields.Float(),
        "goalweight":fields.Integer(),
        "movement":fields.String(45),
        "age":fields.Integer(),
        "gender":fields.Integer(),
        "cycling":fields.Integer(),
        "strength":fields.Integer(),
        "running":fields.Integer(),
        "sports":fields.Integer(),
        "yoga":fields.Integer(),
        "swimming":fields.Integer(),
        "martialarts":fields.Integer(),
        "other":fields.String(45)
    }

)

@api2.route('/clients/profile/<int:clientID>')
class ClientsRescource(Resource):
    @api2.marshal_list_with(genInfo_model)
    def get(self, clientID):
        """Get a client's profile"""
        info = getClientProfiles(clientID)
        return info