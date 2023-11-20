from app import api, app
from flask_restx import Resource, fields
from service.getCoachesService import getCoaches
from flask_jwt_extended import jwt_required


coach_model=api.model(
    "Coaches",
    {
        "email":fields.String(45),
        "firstname":fields.String(45),
        "lastname":fields.String(45),
        "price":fields.Float(),
        "rating":fields.Integer(),
        "experience":fields.Date(),
        "bio":fields.String(4294967295),
        "gym":fields.String(45),
        "town":fields.String(45),
        "state":fields.String(45)
    }

)

@api.route('/coaches')
class CoachesRescource(Resource):
    @api.marshal_list_with(coach_model)
    @jwt_required()
    def get(self):
        """Get all coach profiles"""
        coaches = getCoaches()
        return coaches