from app import api2, app
from flask_restx import Resource, fields
from service.filterWorkoutsByMuscleGroupService import filterWorkoutsByMuscleGroup

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

@api2.route('/workouts/filter/musclegroup/<string:musclegroup>')
class filterWorkoutsByMuscleGroupResource(Resource):
    @api2.marshal_list_with(workout_bank_model)
    def get(self, musclegroup):
        """Filter workouts by muscle group"""
        return filterWorkoutsByMuscleGroup(musclegroup)