from app import api, app
from flask_restx import Resource, fields
from service.getClientGenInfoService import getClientGenInfo
from flask_jwt_extended import jwt_required

genInfo_model=api.model(
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
        "gender":fields.Integer()
    }

)

@api.route('/genInfo/<int:clientID>')
class ClientInfoResource(Resource):
    @api.marshal_list_with(genInfo_model)
    @jwt_required()
    def get(self, clientID):
        """Get General Information by ClientID"""
        info = getClientGenInfo(clientID)
        
        return info