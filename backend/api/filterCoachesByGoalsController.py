# filterCoachesByGoalsController.py
from flask_restx import Resource, fields
from app import api2, app
from service.filterCoachesByGoalsService import filter_coaches_by_goal


coach_model = api2.model(
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


}
  
)
@api2.route('/coaches/filter/goal/<string:goal_type>')
class FilterGoalResource(Resource):
   @api2.marshal_list_with(coach_model)
   def get(self, goal_type):
       """Filter coaches by goal"""
       return filter_coaches_by_goal(goal_type)
