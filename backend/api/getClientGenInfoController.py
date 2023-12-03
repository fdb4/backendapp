from app import api, app
from flask_restx import Resource, fields
from service.getClientGenInfoService import getClientGenInfo

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

@api.route('/genInfo/<clientID>')
class ClientInfoResource(Resource):
    @api.marshal_list_with(genInfo_model)
    def get(self, clientID):
        """Get General Information by ClientID"""
        info = getClientGenInfo(clientID)
        
        return info