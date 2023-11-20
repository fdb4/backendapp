from app import api, app
from flask_restx import Resource, fields
from service.getGenInfoService import getGenInfo
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

@api.route('/genInfo')
class GenInfoRescource(Resource):
    @api.marshal_list_with(genInfo_model)
    @jwt_required()
    def get(self):
        """Get all General Information"""
        info = getGenInfo()
        return info