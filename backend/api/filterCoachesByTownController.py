from app import api, app
from flask_restx import Resource, fields
from service.filterCoachesByTownService import filterByTown
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

@api.route('/coaches/filter/town/<string:town>')
class FilterTownResource(Resource):
    @api.marshal_list_with(coach_model)
    @jwt_required()
    def get(self, town):
        """Filter coaches by town"""
        return filterByTown(town)