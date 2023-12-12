# filterCoachesByExperienceController.py
from flask_restx import Resource, fields
from app import api, app
from service.filterCoachesByExpService import filter_coaches_by_experience

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

@api.route('/coaches/filter/exp/<int:min_experience>')
class FilterExperienceResource(Resource):
    @api.marshal_list_with(coach_model)
    def get(self, min_experience):
        """Filter coaches by experience"""
        return filter_coaches_by_experience(min_experience)
