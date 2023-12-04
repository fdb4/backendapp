from flask_restx import Resource, fields
from flask import Flask, request
from app import api, app
from service.createWorkoutService import createWorkout

@api.route('/workout/create')
class CreateWorkoutResource(Resource):
    def post(self):
        data = request.json
        createWorkout(
            data['workoutname'],
            data['videolink'],
            data['description'],
            data['musclegroup'],
            data['equipment']
        )
        return {"message": "Workout created successfully"}, 201
