from flask_restx import Resource, fields
from flask import request
from app import api
from service.editWorkoutPlanService import edit_workout_plan

# Model for exercise data
exercise_model = api.model(
    "ExerciseData",
    {
        "workoutID": fields.Integer(required=True, description="Workout ID"),
        "Sets": fields.Integer(required=True, description="Number of sets"),
        "reps": fields.Integer(required=True, description="Number of repetitions")
    }
)

# Model for workout plan data
workout_plan_model = api.model(
    "WorkoutPlanData",
    {
        "planName": fields.String(required=True, description="Name of the workout plan"),
        "exercises": fields.List(fields.Nested(exercise_model), required=True, description="List of exercises")
    }
)

@api.route('/edit/workoutplan/<int:workoutplanID>')
class EditWorkoutPlanResource(Resource):
    @api.expect(workout_plan_model)
    def put(self, workoutplanID):
        """Edit a workout plan"""
        data = request.json
        planName = data['planName']
        exercises = data['exercises']
        return edit_workout_plan(workoutplanID, planName, exercises)
