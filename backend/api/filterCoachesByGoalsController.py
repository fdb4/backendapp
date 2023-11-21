from flask_restx import Resource, Namespace, fields
from .filterCoachesByGoalsService import filter_coaches_by_goal

api = Namespace('coaches', description='Coaches related operations')


coach_model = api.model('Coach', {
    'clientID': fields.Integer(required=True, description='The client unique identifier'),
    'email': fields.String(required=True, description='The email of the client'),
    'firstname': fields.String(required=True, description='The first name of the client'),
    'lastname': fields.String(required=True, description='The last name of the client'),
    'price': fields.Float(required=True, description='The price set by the coach'),
    'rating': fields.Integer(required=True, description='The rating of the coach'),
    'experience': fields.Date(required=True, description='The experience start date of the coach'),
    'bio': fields.String(required=True, description='The biography of the coach'),
    'gym': fields.String(required=True, description='The gym where the coach works'),
    'town': fields.String(required=True, description='The town of the gym'),
    'state': fields.String(required=True, description='The state where the gym is located'),
})

@api.route('/filter/goal/<string:goal>')
class CoachesByGoal(Resource):
    @api.doc('list_coaches_by_goal')
    @api.marshal_list_with(coach_model)
    def get(self, goal):
        """
        List all coaches with a specific workout goal.
        """
        return filter_coaches_by_goal(goal)
