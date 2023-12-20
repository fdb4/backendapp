from app import api2, app
from flask_restx import Resource, fields
from service.filterWorkoutsByNameService import filterWorkoutsByName

workout_bank_model=api2.model(
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

@api2.route('/workouts/filter/name/<string:name>')
class filterWorkoutsByNameResource(Resource):
    @api2.marshal_list_with(workout_bank_model)
    def get(self, name):
        """Filter workouts by name"""
        return filterWorkoutsByName(name)