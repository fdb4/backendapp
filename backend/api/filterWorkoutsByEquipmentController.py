from app import api, app
from flask_restx import Resource, fields
from service.filterWorkoutsByEquipmentService import filterWorkoutsByEquipment

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

@api.route('/workouts/filter/equipment/<string:equipment>')
class filterWorkoutsByEquipmentResource(Resource):
    @api.marshal_list_with(workout_bank_model)
    def get(self, equipment):
        """Filter workouts by equipment"""
        return filterWorkoutsByEquipment(equipment)