# filterCoachesByGoalsController.py
from flask_restx import Resource, fields
from app import api, app
from service.filterCoachesByGoalsService import filter_coaches_by_goal


coach_model = api.model(
   "Coaches",
   {
       "firstname": fields.String(45),
       "lastname": fields.String(45),
       "price": fields.Float(),
       "rating": fields.Integer(),
       "experience": fields.Date(),
       "bio": fields.String(4294967295),
       "gym": fields.String(45),
       "town": fields.String(45),
       "state": fields.String(45),


}
  
)
@api.route('/coaches/filter/goal/<string:goal_type>')
class FilterGoalResource(Resource):
   @api.marshal_list_with(coach_model)
   def get(self, goal_type):
       """Filter coaches by goal"""
       return filter_coaches_by_goal(goal_type)
