from app import api, app
from flask_restx import Resource, fields
from service.searchCoachService import searchCoach

coach_model = api.model(
    "Coaches",
    {
        "clientID": fields.Integer(),
        "email": fields.String(45),
        "firstname": fields.String(45),
        "lastname": fields.String(45),
        "price": fields.Float(),
        "rating": fields.Integer(),
        "experience": fields.Integer(),
        "bio": fields.String(4294967295),
        "gym": fields.String(45),
        "town": fields.String(45),
        "state": fields.String(45),
        "specializations": fields.List(fields.String)
    }
)
@api.route('/coaches/<int:coachID>')
class CoachSearchResource(Resource):
    @api.marshal_with(coach_model)
    def get(self, coachID):
        """Get a coach by id"""
        return searchCoach(coachID)
