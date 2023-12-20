from app import api2, app
from flask_restx import Resource, fields
from service.getClientGenInfoService import getClientGenInfo

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
        "gender":fields.Integer()
    }

)

@api2.route('/genInfo/<clientID>')
class ClientInfoResource(Resource):
    @api2.marshal_list_with(genInfo_model)
    def get(self, clientID):
        """Get General Information by ClientID"""
        info = getClientGenInfo(clientID)
        
        return info