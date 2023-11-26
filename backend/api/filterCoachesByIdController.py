# filterCoachesByIDController.py
from flask_restx import Resource, fields
from app import api, app
from service.filterCoachesByIdService import filter_coaches_by_id

coach_model = api.model(
    "Coach",
    {
        "clientID": fields.Integer(),
        "email": fields.String(45),
        "firstname": fields.String(45),
        "lastname": fields.String(45),
        "price": fields.Float(),
        "rating": fields.Integer(),
        "experience": fields.String(),
        "bio": fields.String(4294967295),
        "gym": fields.String(45),
        "town": fields.String(45),
        "state": fields.String(45)
    }
)

@api.route('/coaches/filter/id/<int:coach_id>')
class FilterCoachByIDResource(Resource):
    @api.marshal_with(coach_model)
    def get(self, coach_id):
        """Filter coach by ID"""
        coach = filter_coaches_by_id(coach_id)
        if coach:
            return coach
        api.abort(404, "Coach with ID {} not found".format(coach_id))
