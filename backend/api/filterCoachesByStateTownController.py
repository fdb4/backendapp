from app import api, app
from flask_restx import Resource, fields
from flask import request
from service.filterCoachesByStateTownService import filterByStateTown
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

@api.route('/coaches/filter/statetown/<string:state>/<string:town>')
class FilterStateTownResource(Resource):
    @api.marshal_list_with(coach_model)
    @jwt_required()
    def get(self, state, town):
        """Filter coaches by state and town"""
        return filterByStateTown(state, town)