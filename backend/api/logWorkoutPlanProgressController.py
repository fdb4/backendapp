from flask_restx import Resource, fields, reqparse
from app import api
from service.logWorkoutPlanProgressService import log_workout_progress

log_model = api.model('LogModel', {
    "clientID": fields.Integer(required=True, description="Client ID"),
    "workoutplanID": fields.Integer(required=True, description="Workout Plan ID"),
    "exerciseLogs": fields.List(fields.Nested(api.model('ExerciseLog', {
        "workoutID": fields.Integer(required=True, description="Workout ID"),
        "sets": fields.Integer(required=True, description="Number of sets"),
        "reps": fields.Integer(required=True, description="Number of repetitions")
    })), required=True, description="List of exercises with sets and reps")
})

@api.route('/log/workoutprogress')
class LogWorkoutProgressResource(Resource):
    @api.expect(log_model)
    def post(self):
        """Log workout progress for a client"""
        data = api.payload
        return log_workout_progress(data)
