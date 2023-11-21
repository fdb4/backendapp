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

@api.route('/clients/profiles')
class ClientsRescource(Resource):
    @api.marshal_list_with(genInfo_model)
    @jwt_required()
    def get(self):
        """Get Client profiles"""
        info = getGenInfo()
        return info