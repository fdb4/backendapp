# filterCoachesByRatingController.py
from flask_restx import Resource, fields
from app import api, app
from service.filterCoachesByRatingService import filter_coaches_by_rating

coach_model = api.model(
    "Coaches",
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
        "state": fields.String(45),
        "specializations": fields.List(fields.String)
    }
)

@api.route('/coaches/filter/rating/<string:sort_order>') # Pass "asc" for ascending or "desc" for descending
class FilterRatingResource(Resource):
    @api.marshal_list_with(coach_model)
    def get(self, sort_order):
        """Filter coaches by rating"""
        return filter_coaches_by_rating(sort_order)
