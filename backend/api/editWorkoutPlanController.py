from flask_restx import Resource, reqparse
from app import api
from service.editWorkoutPlanService import edit_workout_plan

@api.route('/edit/workoutplan/<int:workoutplanID>')
class EditWorkoutPlanResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('planName', required=True, type=str, help="Name of the workout plan")
    parser.add_argument('Sets', required=True, type=int, help="Number of sets")
    parser.add_argument('reps', required=True, type=int, help="Number of repetitions")
    parser.add_argument('workoutID', required=True, type=int, help="ID of the workout")

    def put(self, workoutplanID):
        """Edit a workout plan"""
        data = EditWorkoutPlanResource.parser.parse_args()
        return edit_workout_plan(workoutplanID, data)
