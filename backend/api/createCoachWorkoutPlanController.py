from flask_restx import Resource, fields
from flask import request
from app import api, app
from service.createCoachWorkoutPlanService import create_coach_workout_plan

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
        "clientID": fields.Integer(required=True, description="Client ID"),
        "exercises": fields.List(fields.Nested(exercise_model), required=True, description="List of exercises")
    }
)

@api.route('/create/workoutplan/coach')
class CreateCoachWorkoutPlanResource(Resource):
    @api.expect(workout_plan_model)
    def post(self):
        """Create a new workout plan for a client by a coach"""
        data = request.json
        return create_coach_workout_plan(data)

