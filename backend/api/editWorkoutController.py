from flask_restx import Resource, fields
from flask import Flask, request
from app import api, app
from service.editWorkoutService import editWorkout

@api.route('/workout/edit/<int:workout_id>')
class EditWorkoutResource(Resource):
    def put(self, workout_id):
        data = request.json
        editWorkout(
            workout_id,
            data.get('workoutname'),
            data.get('videolink'),
            data.get('description'),
            data.get('musclegroup'),
            data.get('equipment')
        )
        return {"message": "Workout updated successfully"}, 200
