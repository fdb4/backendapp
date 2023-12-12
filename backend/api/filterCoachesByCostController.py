# filterCoachesByCostController.py
from flask_restx import Resource, fields
from app import api, app
from service.filterCoachesByCostService import filter_coaches_by_cost

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

@api.route('/coaches/filter/cost/<float:max_price>')
class FilterCostResource(Resource):
    @api.marshal_list_with(coach_model)
    def get(self, max_price):
        """Filter coaches by cost"""
        return filter_coaches_by_cost(max_price)
