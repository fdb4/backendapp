from flask_restx import Resource, fields
from app import api2
from service.createClientWorkoutPlanService import create_workout_plan

exercise_model = api2.model('Exercise', {
    'workoutID': fields.Integer(required=True, description='Workout ID'),
    'Sets': fields.Integer(required=True, description='Number of sets'),
    'reps': fields.Integer(required=True, description='Number of repetitions')
})

workout_plan_model = api2.model('WorkoutPlan', {
    'planName': fields.String(required=True, description='Name of the workout plan'),
    'clientID': fields.Integer(required=True, description='Client ID'),
    'exercises': fields.List(fields.Nested(exercise_model), required=True, description='List of exercises')
})

@api2.route('/create/workoutplan/client')
class CreateClientWorkoutPlanResource(Resource):
    @api2.expect(workout_plan_model)
    def post(self):
        """Create a new workout plan for a client with multiple exercises"""
        data = api2.payload
        return create_workout_plan(data)
