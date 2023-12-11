from flask_restx import Resource, fields
from flask import request
from app import api
from service.createClientWorkoutPlanService import create_client_workout_plan

# Define the model for the client workout plan
client_workout_plan_model = api.model(
    'ClientWorkoutPlanModel', {
        'planName': fields.String(required=True, description="Name of the workout plan"),
        'clientID': fields.Integer(required=True, description="Client ID"),
        'workoutID': fields.Integer(required=True, description="Workout ID"),
        'Sets': fields.Integer(required=False, description="Number of sets"),
        'reps': fields.Integer(required=False, description="Number of repetitions")
    }
)

@api.route('/create/workoutplan/client')
class CreateClientWorkoutPlanResource(Resource):
    @api.expect(client_workout_plan_model)
    def post(self):
        """Create a new workout plan for a client"""
        data = request.json
        return create_client_workout_plan(
            data['planName'],
            data['clientID'],
            data['workoutID'],
            data.get('Sets', None),
            data.get('reps', None)
        )
