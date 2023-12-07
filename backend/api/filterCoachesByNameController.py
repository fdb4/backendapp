# filterCoachesByNameController.py
from flask_restx import Resource, fields
from app import api2, app
from service.filterCoachesByNameService import filter_coaches_by_full_name

coach_model = api2.model(
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
        "state": fields.String(45)
    }
)

@api2.route('/coaches/filter/name/<string:first_name>/<string:last_name>')
class FilterFullNameResource(Resource):
    @api2.marshal_list_with(coach_model)
    def get(self, first_name, last_name):
        """Filter coaches by first and last name"""
        return filter_coaches_by_full_name(first_name, last_name)
