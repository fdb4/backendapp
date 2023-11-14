from app import api, app
from flask_restx import Resource, fields
from service.getCoachesService import getCoaches

coach_model=api.model(
    "Coaches",
    {
        "clientID":fields.Integer(),
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
    def get(self):
        """Get all coach profiles"""
        coaches = getCoaches()
        return coaches