from flask_restx import Resource, fields
from flask import request
from app import api2, app
from service.editWorkoutPlanService import edit_workout_plan

workout_model = api2.model(
    'Workout',
    {
        "workoutID": fields.Integer(required=True, description="The workout ID"),
        "Sets": fields.Integer(required=True, description="Number of sets"),
        "reps": fields.Integer(required=True, description="Number of repetitions")
    }
)

plan_model = api2.model(
    'EditWorkoutPlan',
    {
        "planName": fields.String(required=True, description="Name of the workout plan"),
        "exercises": fields.List(fields.Nested(workout_model), required=True, description="List of exercises")
    }
)

@api2.route('/edit/workoutplan/<int:clientID>/<int:workoutplanID>')
class EditWorkoutPlanResource(Resource):
    @api2.expect(plan_model)
    def put(self, clientID, workoutplanID):
        """Edit a workout plan"""
        data = request.json
        return edit_workout_plan(clientID, workoutplanID, data)
