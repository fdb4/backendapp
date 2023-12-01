from app import api, app
from flask_restx import Resource, fields
from service.filterWorkoutsByMuscleGroupService import filterWorkoutsByMuscleGroup

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

@api.route('/workouts/filter/musclegroup/<string:musclegroup>')
class filterWorkoutsByMuscleGroupResource(Resource):
    @api.marshal_list_with(workout_bank_model)
    def get(self, musclegroup):
        """Filter workouts by muscle group"""
        return filterWorkoutsByMuscleGroup(musclegroup)