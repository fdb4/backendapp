from flask_restx import Resource, fields
from flask import Flask, request
from app import api2, app
from service.createWorkoutService import createWorkout
womod=api2.model(
    'woModel',
    {
            "workoutname":fields.String(45),
            "videolink":fields.String(300),
            "description":fields.String(10000),
            "musclegroup":fields.String(45),
            "equipment":fields.String(200)
    }
)

@api2.route('/workout/create')
class CreateWorkoutResource(Resource):
    @api2.expect(womod)
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
