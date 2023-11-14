from app import api, app
from flask_restx import Resource, fields
from service.getGenInfoService import getGenInfo

genInfo_model=api.model(
    "genInfo",
    {
        "clientID":fields.Integer(),
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

@api.route('/genInfo')
class GenInfoRescource(Resource):
    @api.marshal_list_with(genInfo_model)
    def get(self):
        """Get all General Information"""
        info = getGenInfo()
        return info