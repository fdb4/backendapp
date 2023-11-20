from app import api, app
from flask_restx import Resource, fields
from service.searchCoachService import searchCoach

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

@api.route('/coaches/<int:coachexpID>')
class ClientResource(Resource):
    @api.marshal_with(coach_model)
    def get(self, coachexpID):
        """Get a coach by id"""
        return searchCoach(coachexpID)