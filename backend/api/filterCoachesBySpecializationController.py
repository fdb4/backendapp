from app import api2, app
from flask_restx import Api, Resource, fields
from service.filterCoachesBySpecializationService import filterBySpecialization


coach_model = api2.model(
    "Coach",
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

@api2.route('/coaches/filter/specialization/<string:specialization>')
class FilterSpecializationResource(Resource):
    @api2.marshal_list_with(coach_model)
    def get(self, specialization):
        """Filter coaches by specialization"""
        return filterBySpecialization(specialization)
