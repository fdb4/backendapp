from app import api, app
from flask_restx import Resource, fields
from service.filterWorkoutsByNameService import filterWorkoutsByName

workout_bank_model=api.model(
    "Workout_Bank_Model",
    {
        "workoutID":fields.Integer(),
        "workoutname":fields.String(45),
        "videolink":fields.String(65535),
        "description":fields.String(65535),
        "musclegroup":fields.String(45),
        "equipment":fields.String(45)

    }

)

@api.route('/workouts/filter/name/<string:name>')
class filterWorkoutsByNameResource(Resource):
    @api.marshal_list_with(workout_bank_model)
    def get(self, name):
        """Filter workouts by name"""
        return filterWorkoutsByName(name)