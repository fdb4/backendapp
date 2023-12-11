from app import api
from flask_restx import Resource, reqparse
from service.createClientWorkoutPlanService import create_client_workout_plan

@api.route('/create/workoutplan/client')
class CreateClientWorkoutPlanResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('planName', required=True, type=str, help="Name of the workout plan")
    parser.add_argument('clientID', required=True, type=int, help="Client ID")
    parser.add_argument('workoutID', required=True, type=int, help="Workout ID")
    parser.add_argument('Sets', required=False, type=int, help="Number of sets")
    parser.add_argument('reps', required=False, type=int, help="Number of repetitions")

    def post(self):
        """Create a new workout plan for a client"""
        data = CreateClientWorkoutPlanResource.parser.parse_args()
        return create_client_workout_plan(data)
