from flask_restx import Resource, fields
from app import api
from service.editWorkoutPlanService import update_workouts_in_plan

@api.route('/workoutplan/update/<int:workoutplanID>')
class WorkoutPlanUpdateResource(Resource):
    @api.expect(api.model('WorkoutPlanUpdate', {
        'workouts': fields.List(fields.Nested(api.model('WorkoutUpdate', {
            'id': fields.Integer(required=True, description='Workout Plan Entry ID'),
            'workoutID': fields.Integer(required=True, description='Workout ID'),
            'Sets': fields.Integer(required=True, description='Number of Sets'),
            'reps': fields.Integer(required=True, description='Number of Reps')
        })))
    }))
    def put(self, workoutplanID):
        data = api.payload
        return update_workouts_in_plan(workoutplanID, data['workouts'])
