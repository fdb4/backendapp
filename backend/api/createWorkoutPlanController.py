from app import api, app
from flask_restx import Resource, reqparse
from service.createWorkoutPlanService import create_workout_plan

@api.route('/workoutplan/create')
class CreateWorkoutPlanResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('planName', required=True, type=str, help="Name of the workout plan")
    parser.add_argument('clientID', required=True, type=int, help="Client ID")
    parser.add_argument('workoutID', required=True, type=int, help="Workout ID")
    parser.add_argument('Sets', required=False, type=int, help="Number of sets")
    parser.add_argument('reps', required=False, type=int, help="Number of repetitions")

    def post(self):
        """Create a new workout plan"""
        data = CreateWorkoutPlanResource.parser.parse_args()
        return create_workout_plan(data)
