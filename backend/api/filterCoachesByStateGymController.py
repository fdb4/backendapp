from app import api, app
from flask_restx import Resource, fields
from service.filterCoachesByStateGymService import filterByStateGym
from flask_jwt_extended import jwt_required

coach_model=api.model(
    "Coaches",
    {
        "clientID":fields.Integer(),
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

@api.route('/coaches/filter/stategym/<string:state>/<string:gym>')
class FilterGymResource(Resource):
    @api.marshal_list_with(coach_model)
    @jwt_required()
    def get(self, state, gym):
        """Filter coaches by state and gym"""
        return filterByStateGym(state,gym)